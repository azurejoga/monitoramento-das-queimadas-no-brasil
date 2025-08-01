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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14d545c6-84fa-32e0-9089-6dd615f6e968 | -7.7405 | -45.06881 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c268cc3-d4cb-3e59-bd30-1e22232a4eb5 | -12.65775 | -48.09406 | 2025-08-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 34f6abcc-2ef9-3e6e-bd40-480d02998a3f | -8.03771 | -43.11735 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.4 |
| 2cb49afe-8618-3848-994f-6f06f5ace5e4 | -9.45364 | -57.8372 | 2025-08-01 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fee1466a-aee4-3665-93b6-fbaa9015e4a0 | -7.72285 | -45.09205 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d738487-8bcc-333c-87f8-c5285fb28e41 | -8.29083 | -47.34368 | 2025-08-01 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a08f794-af56-3f9c-83c5-28f42d61fce0 | -9.73963 | -48.66502 | 2025-08-01 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c477a263-622d-3a2e-913d-c04cb94479a9 | -7.25096 | -43.39119 | 2025-08-01 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 35f15007-4f7a-347c-b85c-d8e5e44c53cb | -7.26695 | -43.39725 | 2025-08-01 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5786e5b7-4839-3efa-8b3b-754c6b13d08e | -10.79507 | -47.25887 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1357f385-7389-393f-8edb-600220bdda54 | -12.55955 | -44.73078 | 2025-08-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e051c02e-c232-39e9-a2d5-fe405e113a38 | -8.33152 | -50.57726 | 2025-08-01 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 35847466-f7a7-3afb-a3d2-b5f2c7ab635d | -7.26419 | -43.39328 | 2025-08-01 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 9bd2f3fa-86a5-3b76-9cf1-1b4296cb3e9d | -7.03379 | -43.28205 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 600b0dda-32c3-32ea-843d-e35fc5fc4d4a | -11.8125 | -48.79165 | 2025-08-01 04:14:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b63eb67-d953-3235-9e2b-d21f4632ec84 | -12.43807 | -44.74674 | 2025-08-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70780cd1-4cad-33cb-b88c-1cf42fbe3b84 | -9.45929 | -57.84549 | 2025-08-01 04:14:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b134b551-d3b8-322c-a2b8-af652a61cddb | -7.73079 | -45.08587 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4417f08-286d-3dae-bcfd-303f99e58937 | -10.79864 | -47.25952 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cde60710-a46c-33bb-9bb4-6f221118866a | -11.54422 | -44.32038 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fd219ba9-e7e5-3a86-9e47-0a741cea4305 | -8.29157 | -47.3392 | 2025-08-01 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7554356-aa73-39f5-9cb5-f5f22ce00854 | -6.55354 | -56.19545 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4947b5fb-5a48-3f39-90e4-c3f2faad040e | -11.16504 | -45.7577 | 2025-08-01 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d4528ad-6e65-33a1-b73c-7c20a8cbfbe0 | -8.04819 | -43.11543 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 69b3b2bc-d234-3ce0-97f5-927ac6ccde5e | -7.73991 | -45.07244 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 20d183df-94aa-3eec-bdec-5e4aea52ca96 | -11.77189 | -45.00606 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9afa1d23-c18c-378b-853c-f5c966e1599d | -9.81505 | -47.75386 | 2025-08-01 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 136cc476-6f14-3bd0-88e6-644932afabd1 | -6.52014 | -56.21146 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b20010ac-6967-3704-99ba-69820a183d3b | -10.06193 | -48.33323 | 2025-08-01 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b976da4a-c670-3a16-960e-351ac65b80e4 | -12.43752 | -44.75026 | 2025-08-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 472aeef8-a800-3bc4-bbe1-2f75ed5e0912 | -7.24766 | -43.39066 | 2025-08-01 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a404f5e0-6fd1-327a-8f58-b68d3f70b34f | -10.10306 | -58.23381 | 2025-08-01 04:14:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6531ed6a-231e-3c7c-8763-079ea3301843 | -7.14688 | -43.27514 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e804f7a5-aea0-39b3-8857-a882ea2833c1 | -12.22087 | -44.2499 | 2025-08-01 04:14:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8b9e4360-4b13-39a4-9673-de328bf66de7 | -9.40114 | -45.49644 | 2025-08-01 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16e5760b-f98a-3402-a572-3bfa4eba511e | -6.55248 | -56.18686 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eb5431df-6ef4-338c-b879-7a29598736b3 | -10.60435 | -45.27348 | 2025-08-01 04:14:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5a4d385e-65e5-3c76-ac77-a7a982a6e88b | -6.56023 | -56.19688 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0bac3ee-011b-3ec6-9fa3-e26c66726610 | -9.74356 | -48.66567 | 2025-08-01 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d50d35c4-d3e2-3c5c-a9d7-8c5cf9cf26f8 | -8.05313 | -43.10551 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| d22b57d3-6910-3ab2-b648-5e47bd409615 | -7.34811 | -44.17119 | 2025-08-01 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b379a63-33fe-3855-a58d-6aa3e5e18111 | -12.55625 | -44.73024 | 2025-08-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e51a6590-5a2a-332a-82d0-827c355e9a5c | -13.22509 | -47.23605 | 2025-08-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 05348832-b44b-3c30-93b2-0d51e36e3f7d | -7.27922 | -43.05828 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ea3e723b-4957-3dd5-be26-515890671cae | -7.14358 | -43.27461 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ee6f1b1f-3089-3274-a96f-380ec25c3277 | -9.85588 | -44.70444 | 2025-08-01 04:14:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e44f4bb-6792-322f-a885-827c5a7aca94 | -13.36909 | -43.75856 | 2025-08-01 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10d7fa4d-b7c1-3a6c-9d01-2852f497607a | -11.76091 | -44.98957 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 627b125e-8f35-3341-9d4a-6317d3e3196d | -7.72682 | -45.08896 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97c7ec27-4890-36cb-9ad2-3168a477dd32 | -11.76364 | -44.99385 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e64486c2-fdb5-3b57-a43f-615d090b8df6 | -10.69861 | -48.87065 | 2025-08-01 04:14:00 | NOAA-20 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1179878e-d2dc-3544-9267-13a37f10c22b | -8.51571 | -43.31755 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 734becc0-26ff-35a6-91ad-f0a73f23e579 | -13.51331 | -45.63187 | 2025-08-01 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bc71aa1-2838-3e9c-8079-598af3420413 | -11.58735 | -41.6922 | 2025-08-01 04:14:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bda18857-da9f-3290-8bef-7fa578439b04 | -8.41123 | -47.50478 | 2025-08-01 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e805b223-9e37-30e1-a944-e16833d0c3fc | -12.6549 | -48.08861 | 2025-08-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44b5b21d-27c8-369b-aa2c-25c0b0412f02 | -11.52311 | -44.32483 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc1ea37a-351b-3e2b-a0ca-8936f6bcd058 | -12.42599 | -44.7159 | 2025-08-01 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad4137ad-2317-3553-bd70-ea02b2822891 | -13.21394 | -47.23858 | 2025-08-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a7a4dfc6-8380-3ff3-b236-96daa9ea9071 | -6.92452 | -43.15455 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f0aea45b-b4a2-32bc-b014-92a718ab81d2 | -7.53484 | -43.82984 | 2025-08-01 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1475628-7e5f-372a-9f51-fc1fdb9d2daa | -6.83914 | -42.83271 | 2025-08-01 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 60df0a85-4e0b-3334-9e6d-1dc5c285edc1 | -11.75816 | -44.98551 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52948b72-0e1b-3e48-a245-42a50049717b | -12.42929 | -44.71644 | 2025-08-01 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38c623c3-7754-30eb-9003-059567658bff | -6.5145 | -56.20431 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e99596c8-6dbf-3748-be58-2e5c4c4bfd1e | -11.768 | -45.00907 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c35972dc-1ea1-366b-8191-61c49111f646 | -5.05875 | -56.93055 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b63d0c98-9c78-3582-8011-4a5f24c227d6 | -9.79797 | -47.05769 | 2025-08-01 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3178a78b-6bb0-3f49-a9eb-910722736b1d | -7.35199 | -44.16822 | 2025-08-01 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3f7742a-2b5e-333a-8cea-bcde201f6594 | -11.54186 | -44.31348 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2c886e48-0fd3-378f-b284-8f8d72ec2d14 | -11.58482 | -48.17661 | 2025-08-01 04:14:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb96dd7d-eec8-31c3-b0a1-68c2b8ade851 | -7.58924 | -44.80834 | 2025-08-01 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d1e35fa-92b0-34f7-80d7-8c8a35a3c50a | -11.58794 | -41.68819 | 2025-08-01 04:14:00 | NOAA-20 | LAPÃO | BAHIA | Brasil | 2919157 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e5f419f8-19f2-3c67-98d1-e7977a9152af | -6.53113 | -56.20348 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1666260-ba7b-3902-9cd5-4fee5c6f4c49 | -6.50891 | -56.19688 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f882ae2f-0f51-375b-ac08-a34413152a52 | -11.59331 | -46.44608 | 2025-08-01 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2e014924-29da-3e94-9f93-f719024b50b1 | -10.43643 | -47.25279 | 2025-08-01 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68d29b81-ec15-3e2a-a3aa-1d6795603606 | -8.91744 | -47.33896 | 2025-08-01 04:14:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5e4c222-8aea-3af8-8892-2ccc02cc570b | -7.30733 | -43.7862 | 2025-08-01 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9549bc8-f000-3fa9-a55c-4fb9c6cd8fc3 | -7.72741 | -45.08533 | 2025-08-01 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22fd44dc-d53d-318d-9e8b-6165ce2ca988 | -13.21744 | -47.23905 | 2025-08-01 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46af69c9-1d12-3d41-b7e7-b41fb489c42e | -6.54569 | -56.20015 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fc98a07a-a549-3399-b638-91e9bec5bf48 | -12.64606 | -48.09661 | 2025-08-01 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 36e4199f-b537-31eb-86a3-9757e5772b13 | -8.32717 | -50.57749 | 2025-08-01 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5e44af4-e5ef-371b-9091-64746d52f71c | -8.5124 | -43.31702 | 2025-08-01 04:14:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 00e8ce0f-2d07-34ce-9eed-5c4d4640343a | -11.52808 | -44.29328 | 2025-08-01 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36552e0f-0b62-3644-914a-7a6e4d0dcdde | -7.53429 | -43.83331 | 2025-08-01 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4f39c1b-d463-3a0a-8c94-1f8f962ae3dd | -6.56137 | -56.19082 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88ee3e24-179f-3cf8-82a7-cf1c1ca59fc9 | -7.04607 | -44.40405 | 2025-08-01 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 807bd0f6-65a4-3a53-a360-dc40644b281e | -12.55294 | -44.7297 | 2025-08-01 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 730baaad-f6dd-3ceb-b7c0-b4a7b69c290a | -6.52685 | -56.21285 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41ed75b8-1335-3ff3-9119-ce2759111799 | -13.197 | -48.32001 | 2025-08-01 04:14:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fd5d94a0-a6b0-3cfb-8fcf-5b1b30f29926 | -8.33073 | -50.58193 | 2025-08-01 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f82b3661-fd22-3ad7-92a4-c3e05e316bce | -11.77577 | -45.00306 | 2025-08-01 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2941c4f5-1c9e-3d1e-8e1b-672a4cc356ef | -9.0195 | -47.9769 | 2025-08-01 04:14:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99db91e1-0c4a-332e-b61f-6680c04ef9f3 | -12.26811 | -45.06943 | 2025-08-01 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf2d2c73-56b0-3295-a6da-8b4e2a2ec482 | -9.46889 | -47.80201 | 2025-08-01 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6789ba5c-a351-3aa1-82e3-ff6b45117d5e | -12.7514 | -44.41874 | 2025-08-01 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd3cfc60-e03b-31f7-ad7c-6f004d676cde | -6.52327 | -56.20818 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efecafc2-5460-36d7-981b-f3e52c834636 | -6.55466 | -56.18953 | 2025-08-01 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README16.md)
