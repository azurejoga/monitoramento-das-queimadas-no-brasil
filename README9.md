# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b582bfd7-3f93-354f-88be-df697206d142 | -2.88759 | -48.0135 | 2026-08-01 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c932011d-0995-32ac-ae56-b8838bd1d8f5 | -2.32763 | -47.20284 | 2026-08-01 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04542c62-4590-3184-817d-663cd10f33c7 | -5.04253 | -43.26299 | 2026-08-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f81b5a72-0e8b-3f7b-9a26-636674f8890f | -7.21721 | -43.55637 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a2096c2d-5191-367b-94d9-64888ef3c7b2 | -7.19846 | -42.96735 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 928381b0-d600-372c-9a9d-4b0c3cd380cb | -3.05119 | -48.74376 | 2026-08-01 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9c5420a-54e9-316e-a67c-e62c46c6c0dc | -7.55096 | -43.9934 | 2026-08-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 905898ff-6cb5-3ea5-ba23-64f8132fb0c0 | -7.61084 | -42.58596 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e0962547-7b77-3125-a680-984184fd59c4 | -3.11356 | -47.91259 | 2026-08-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6f87b38a-63ea-3ff0-a8fb-3a6a01b03fe4 | -3.56324 | -43.20002 | 2026-08-01 04:19:00 | NOAA-21 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34f13c8b-7caa-3b0b-bd15-582f9c13ebda | -7.23432 | -44.37048 | 2026-08-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36c1a20a-b908-3a24-bba4-5c76a2cafb16 | -6.75892 | -41.01699 | 2026-08-01 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 95f396f9-7b1e-3093-997c-d811f04f3af9 | -7.23311 | -44.5337 | 2026-08-01 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7bc66f3-0353-3114-81be-2808b7f031d6 | -6.65156 | -43.91869 | 2026-08-01 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d1a878ac-654d-3171-8a73-68d7e70d6588 | -7.24043 | -43.42738 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b6222942-0772-3b22-bd0a-883e61e47fdf | -6.77259 | -41.83099 | 2026-08-01 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 96a0501e-6ae6-345c-ae19-c2798cd5788b | -2.16155 | -47.87012 | 2026-08-01 04:19:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c13626c4-0def-358a-99a3-4e9938e4271f | -7.32186 | -43.00894 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6102d335-77ed-3831-ab5b-571e4b1d8cff | -6.85172 | -42.87376 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 50287dbb-2bc2-338c-bc4a-227f31a1d89c | -6.84437 | -42.89922 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3f1fa2e1-c1bd-3134-a787-2f92224de2c4 | -7.66775 | -45.06008 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff2c7a21-347c-3da4-aa06-02e93075cd0a | -6.52413 | -42.76794 | 2026-08-01 04:19:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 026e0608-e195-3f84-9b2a-62b06b6b2d86 | -8.31541 | -44.78941 | 2026-08-01 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03bcc7cb-f038-3caf-88c8-54d70f570f1c | -3.80122 | -41.61027 | 2026-08-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 37887ca8-377a-3455-a716-634313e3da0c | -3.03376 | -48.40629 | 2026-08-01 04:19:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6ebf6f51-9ae1-3832-97c1-f2039e26130c | -5.73132 | -44.50282 | 2026-08-01 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7a44b57-1b28-34b1-b12c-c1da92b9ea47 | -4.65028 | -42.43192 | 2026-08-01 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1da1d9f7-3fed-3ae6-9a5a-3aee82e42777 | -7.66391 | -45.06303 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1cc305c-ac93-30c7-91c0-cb660f2d6558 | -3.72771 | -49.27633 | 2026-08-01 04:19:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f26a16d-682a-3cab-a221-4b4adb24e9aa | -3.05267 | -48.74097 | 2026-08-01 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae3df7ab-241d-3361-b8da-d619c2a7d7ad | -7.6457 | -45.04955 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22db7da7-14c8-3a83-b659-f725a2e5d14b | -4.6537 | -42.43244 | 2026-08-01 04:19:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6d0e704c-27ac-391f-b7fb-f5d0137b7813 | -3.84938 | -44.09412 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af2126e2-4be6-38f0-b220-29632ab2afda | -6.76524 | -41.0111 | 2026-08-01 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3ec061cd-4b69-3c30-a26a-3c5da9179b61 | -3.86259 | -44.09616 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f11fb73-4353-3688-8d37-b9b99ff27251 | -5.93454 | -46.34974 | 2026-08-01 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1491c5b-a9e4-36d7-ac99-b619a38539aa | -6.64878 | -43.91468 | 2026-08-01 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a656949c-0eab-3b16-a1cf-01e3f47e8824 | -4.00163 | -43.2898 | 2026-08-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa409fa4-02f0-3ad9-bf3f-e3e08ca8fdd1 | -7.54817 | -43.98936 | 2026-08-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b941f2fb-70b1-3270-8283-8f295fa6b55d | -7.24822 | -42.13672 | 2026-08-01 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 28034c1e-89f7-334b-8204-f7cb04777d98 | -2.89139 | -48.01411 | 2026-08-01 04:19:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9886d58c-9558-321f-b099-69bd53c70406 | -6.71831 | -44.01485 | 2026-08-01 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 90c2a39d-4226-32e0-9967-bdfd8406570d | -7.64954 | -45.0466 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b6ffe80-91fd-3083-9676-e148c8b8c03b | -4.2868 | -48.24591 | 2026-08-01 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 740d2f60-14a3-3e8b-9fa7-8088d6e2cc84 | -6.10438 | -55.80721 | 2026-08-01 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ed3217d-03d8-37de-9620-eb0549786daf | -6.28464 | -41.85329 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0b53ff5c-6c48-382e-9168-4059947d526c | -3.85268 | -44.09463 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f637fe16-73d1-3962-ae7d-e37a7b7013eb | -3.85214 | -44.09807 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5c0bb10-fdc2-3105-8263-789c18070197 | -3.80181 | -41.60638 | 2026-08-01 04:19:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 45bdb996-00a9-3093-acb8-bebe9a6e237a | -6.72163 | -44.01536 | 2026-08-01 04:19:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3a1ac3a4-fc5b-3a17-8f6e-4226730c4f80 | -5.25455 | -38.23181 | 2026-08-01 04:19:00 | NOAA-21 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf34a659-3b74-342f-a78d-85a040ef967c | -3.06101 | -39.92545 | 2026-08-01 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 28ca7313-d894-3418-943d-840a96165752 | -6.86707 | -44.78783 | 2026-08-01 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62b4fa53-471b-3661-ad2c-43e4a481222e | -3.85875 | -44.09909 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deb53abe-f7c0-3dc1-b071-9b82785ccdc9 | -7.5543 | -43.99391 | 2026-08-01 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25940e23-d038-3205-b61e-b55b089a1b16 | -7.34378 | -43.00415 | 2026-08-01 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 73f956b1-46bb-3ab8-b5f0-062e865ed0b4 | -6.54156 | -41.85176 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c6947fca-8031-3f3f-a15d-16d7e0485df1 | -7.60735 | -42.58543 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 918cd2f4-7954-33af-9521-b3ee9574bf7f | -4.64611 | -43.12284 | 2026-08-01 04:19:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34e73cf2-5c6a-33cc-850d-469810008069 | -7.32242 | -43.00522 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d81dbc07-90dc-37bf-bafc-75a7133af47f | -7.01326 | -45.84788 | 2026-08-01 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 995d0632-d3ea-3e44-8e38-a54811cd2801 | -6.76087 | -41.01501 | 2026-08-01 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| efbe38d0-5d0f-3ebe-86bb-58ab278ba3f7 | -4.61483 | -49.0561 | 2026-08-01 04:19:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7dbcf899-c530-3f20-8f90-1f4fee65145f | -4.52619 | -38.5475 | 2026-08-01 04:19:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 698f0b2a-cce0-318a-b021-3979a6d99d91 | -6.09573 | -44.89227 | 2026-08-01 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3430779-e730-3028-9d22-cb52cc5c3b9a | -6.55713 | -55.15751 | 2026-08-01 04:19:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 45348878-0900-30ca-8143-b8a14d4ecccb | -7.03821 | -43.21471 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8c6b3294-6dcb-39da-8b29-ce04bf0267d4 | -7.65285 | -45.04712 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfb838dc-7cbb-3594-962d-17fb06d4dcb3 | -4.37073 | -47.77056 | 2026-08-01 04:19:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1174814e-9d07-3604-86c1-1e025570d8d6 | -7.2036 | -42.97951 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ed9c2c7d-fa98-33e8-9466-8ff79b723ae3 | -3.85375 | -44.08776 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a3edd98-e69d-3bfd-bf4a-f77fe646034a | -6.78154 | -41.81984 | 2026-08-01 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 076aa836-9965-32da-98d2-bcfa7404ac26 | -5.76641 | -47.34336 | 2026-08-01 04:19:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dd108a05-e973-3a2f-8f33-7c58f3cf0cd3 | -7.1956 | -42.96313 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 14eeb61e-ccac-38cf-8977-cbf3e986e37a | -6.18686 | -44.85359 | 2026-08-01 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c8b6d9e-406c-37de-b38c-15ab8e17dd12 | -6.76654 | -41.00214 | 2026-08-01 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8e9ff0d-c9a8-3eca-bcb6-4f6797d785ce | -6.26976 | -41.87973 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7f158f6d-95ce-3b25-92ae-ebf31adc1643 | -3.9983 | -43.28929 | 2026-08-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 289da9a5-6130-32d7-ac47-8bc88971c421 | -6.77972 | -41.83215 | 2026-08-01 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 808e8539-9f45-3e02-972d-95d9d43bffe8 | -6.55044 | -41.8655 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3d75985-fc25-325d-b262-b466ec857eb5 | -5.73186 | -44.49937 | 2026-08-01 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53ee654a-57f4-3b87-a88e-a71d55d61565 | -7.24099 | -43.42376 | 2026-08-01 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4929c466-d126-32b5-aaea-350c8fd62e71 | -7.64846 | -45.05352 | 2026-08-01 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 252e991c-989d-32ca-918c-d44ee7a0429c | -6.55461 | -41.83736 | 2026-08-01 04:19:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bb7a7786-1eab-35f7-baa9-3da622dc9808 | -6.76216 | -41.00605 | 2026-08-01 04:19:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3843b9d7-76db-3472-b162-7cb3e9fcddcf | -4.00047 | -43.27532 | 2026-08-01 04:19:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f504dea-ce44-38c5-8ec3-65f24ba35504 | -6.77402 | -43.03627 | 2026-08-01 04:19:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 250c8d97-2be0-3054-ba74-8e6c5fe12614 | -6.42491 | -42.8217 | 2026-08-01 04:19:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 046714ed-4938-33eb-b7c4-e22794e4fe11 | -5.81362 | -44.75922 | 2026-08-01 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 455e2545-b02d-3131-9cd8-45d2138edeb8 | -7.83846 | -47.09519 | 2026-08-01 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 600b5641-dfbe-30e3-b2c0-4d3b6f2fba6d | -3.48025 | -47.68603 | 2026-08-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2218e779-df83-3bdf-b12d-1dfd4319322f | -3.11429 | -47.90808 | 2026-08-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aedcf556-4f6f-3c30-a37c-0cb3b772995e | -6.67362 | -42.56704 | 2026-08-01 04:19:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| ed9064f7-2dcc-330c-afb7-b07d0de57251 | -2.32743 | -47.20329 | 2026-08-01 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e20128ac-36ea-3179-ad0c-cd521c03c587 | -6.77615 | -41.83157 | 2026-08-01 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 957bbfa9-701d-3edd-b640-d9dc7570203a | -5.74196 | -41.00885 | 2026-08-01 04:19:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e76229be-b525-37f1-84c5-62ae6ae78fde | -3.05722 | -39.92489 | 2026-08-01 04:19:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6809a450-a680-3f2c-9c8c-ebd5d5f7bc42 | -6.79462 | -41.83015 | 2026-08-01 04:19:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4aca5e34-ce6a-31ba-b9af-f334ad0dd60a | -3.1098 | -47.91203 | 2026-08-01 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 18ebb97c-e955-3685-84d9-7ca2b36c045d | -3.85045 | -44.08725 | 2026-08-01 04:19:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README10.md)
