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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b258cddc-bdb3-3b98-a06b-a58a6b1901a8 | -3.89358 | -42.51289 | 2025-09-16 04:27:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 298765ad-e1de-3aa0-9e5c-0c0498008ff3 | -2.29699 | -48.14543 | 2025-09-16 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef5542c8-f17c-3d61-b72f-6fee6db4f85c | -6.64941 | -44.71494 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18521300-a950-3e7f-9ed7-6867a5df9cb4 | -5.78684 | -45.93276 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75a44f60-b6a4-3718-bdf8-20c53cabd34b | -6.62179 | -44.73353 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1688acaa-a9c0-3791-9413-024bfdb3e9cc | -6.46774 | -46.03626 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dce6103-7f3d-3d74-ba8e-ecb67102cc3a | -3.9937 | -43.23917 | 2025-09-16 04:27:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b31f731-4c2e-3e7d-8632-96b2753ff5c0 | -5.89119 | -45.74633 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb4f49a1-3756-3b96-aa3a-b6271df722d1 | -6.40332 | -44.01008 | 2025-09-16 04:27:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34ff2aeb-5209-3dce-bb62-b1ba92c463fa | -7.0847 | -44.55753 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d2b803d-47c7-36eb-9898-fdd522ae1b8f | -5.78298 | -45.9393 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bfbbc3d-13f7-3c1f-abbe-5adcc32aa2c7 | -6.88108 | -45.62186 | 2025-09-16 04:27:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cbbf8c67-dbe7-355c-a325-be83f6a8c880 | -5.77845 | -45.90308 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8945e680-b1a9-35aa-ad26-622d21994985 | -7.01603 | -44.52839 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88ad9355-e7a9-377b-b080-f061556232e0 | -5.77618 | -43.92458 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d021d4cb-1092-31db-b17c-9b8d598df417 | -6.28703 | -42.38774 | 2025-09-16 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 142f7d90-544e-3001-b213-1067d2183a4f | -7.01145 | -44.53531 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80670b94-5d8b-38f3-8c4c-5cb54128c7fe | -6.78715 | -44.7474 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 281c50fb-51ba-3773-bbe3-48164d60bf09 | -5.76478 | -52.37089 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 976773ad-8d27-3e2f-a671-5048cfb1c190 | -5.79682 | -45.93433 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a6f3633-341d-3559-87dd-868e739db13d | -3.83164 | -44.10155 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31159083-3047-33b0-9294-879426c331b3 | -5.79017 | -45.93329 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74805cf7-3fb9-30db-b935-ef10f38c31f5 | -5.77503 | -43.93219 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e87500f-9428-3b21-95da-85309d083f42 | -5.89687 | -49.10042 | 2025-09-16 04:27:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 627e00f3-e5e3-329f-ad70-4904a1005aa7 | -7.49644 | -44.67278 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ccfb56e-2826-31ae-a45e-909a8bb341e2 | -6.18991 | -41.18372 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ba221ede-3f08-3cde-9d7b-de9ae6662434 | -6.52658 | -41.82933 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e4e15901-b2bf-3297-b26e-deb522619954 | -5.99306 | -43.70528 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36c4e2fb-db4a-3233-8157-1c79a2369151 | -5.26483 | -43.78309 | 2025-09-16 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6897e73-e38a-306c-afb8-c1a9c000203a | -5.76066 | -43.69477 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f538a096-0b05-3541-8f61-a5b9592627cf | -5.05352 | -45.19715 | 2025-09-16 04:27:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a6857e6-d67b-39e5-ab74-e549442495c4 | -3.80949 | -41.55441 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 88de0515-74f2-32cb-991c-9595632304ce | -5.93662 | -45.71041 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b0c5e53-5aac-3849-a2a4-8b05f202c76b | -7.22141 | -47.0047 | 2025-09-16 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f33d126-02c0-3875-8f46-01d19e8e5701 | -6.88226 | -46.06592 | 2025-09-16 04:27:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acdc7882-e31d-3b7d-bb15-7834c94a857d | -3.42023 | -43.15131 | 2025-09-16 04:27:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 40f64562-f0ef-3fab-8303-bfbbb8930252 | -6.14403 | -43.35327 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0ebd8c4-2208-33de-a1b0-948c07b3a573 | -3.80806 | -41.56379 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9b6c9922-a654-3e15-9fac-ec033bf3ae09 | -7.31513 | -43.96 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d07b1968-030d-3d3c-ad97-319d05e47e96 | -7.26667 | -46.61145 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c62b0906-e4e7-3537-aff2-488cce370071 | -5.85089 | -44.16801 | 2025-09-16 04:27:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a72d7d94-a246-343f-a3e2-c9409cf0ada3 | -6.68544 | -46.30942 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7e078203-3ae0-3ef9-b36e-bce44e207448 | -6.15835 | -45.11588 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 828a008c-8cc1-3c3f-a557-2ff0d24f0165 | -6.97144 | -44.56736 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b2df1ea-b046-3aff-8dda-5113efc68301 | -6.97349 | -44.53801 | 2025-09-16 04:27:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ea4eb85-1319-3f1e-b153-0f741e859589 | -3.21379 | -47.1304 | 2025-09-16 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| dc8dca99-1b76-3350-bf2d-4b6e2c1a983c | -3.30995 | -42.16862 | 2025-09-16 04:27:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 31649623-1766-3d23-aaec-a672f292c9fb | -7.08639 | -44.54645 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6c59823-49ee-309a-bd8f-a4d4f506feca | -3.22155 | -47.12754 | 2025-09-16 04:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 248e1a37-a9e6-3781-8e76-3155e8e39c65 | -5.77615 | -43.91764 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4469bb4b-c5d9-3074-b639-4f9b62654d46 | -6.16416 | -43.66969 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aa6b0a7-2674-356d-8514-f72ac76edd81 | -6.54562 | -44.00303 | 2025-09-16 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8c316c90-daef-38bf-966f-97d859e6c414 | -5.89562 | -45.7399 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eaee6178-8951-342b-93c6-1677b0993686 | -7.43828 | -45.83801 | 2025-09-16 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30042887-a671-3ea0-b346-209e415ff4d7 | -7.31454 | -43.96389 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e89c6998-bb7c-36ea-8461-a2fc133de559 | -7.31631 | -43.95221 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ee1ef09a-f7f4-3bb3-b231-bd2b670a6ffa | -7.08982 | -44.547 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f90ce44c-7066-3bea-ad13-bccdeaedce93 | -5.34654 | -44.8158 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df47dc5d-408a-3904-98d8-33606af3ef38 | -6.52978 | -41.83477 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 523c255a-2ed5-38dd-9e08-b8399255543e | -7.66488 | -44.4789 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23483713-ecbb-302c-9e83-4a39704cbbfe | -5.79404 | -45.93039 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 145a1dbd-52d7-3596-ba9a-c0fb7d20429c | -5.83378 | -45.26822 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d641ff-4ed1-3389-888a-6324be63f760 | -3.5703 | -51.56417 | 2025-09-16 04:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ae9f0d0-4e8b-37cb-8704-40f5b760bf49 | -3.82258 | -44.11501 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7f2d280-70de-3d4c-9922-28929302fd7d | -5.83934 | -44.15857 | 2025-09-16 04:27:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52f27893-c5e0-30f1-a503-0e247d38f3ab | -7.08412 | -44.54288 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68e0b1dc-e783-3599-9bcd-48d74aeeced9 | -6.17549 | -46.81704 | 2025-09-16 04:27:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 772de240-d65c-3b19-97be-7504d7f6c06a | -6.41353 | -44.36634 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd0f61c5-541e-34b2-b1ba-2407e846877a | -5.90552 | -45.90852 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89b884e5-a09e-3e96-83fa-f989a278ec94 | -5.95576 | -42.80417 | 2025-09-16 04:27:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 73267c79-5fe8-3377-b909-e7d5565076f8 | -7.01552 | -44.89354 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07e0a9c7-14af-3921-8753-eb15ac0b73fe | -7.28104 | -46.58521 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a04f428f-30b2-3786-952a-617f22d269a8 | -5.05632 | -45.20118 | 2025-09-16 04:27:00 | NPP-375D | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f142241b-7f97-3095-be74-f420ffdd7866 | -3.73822 | -49.04941 | 2025-09-16 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a74ae26c-ee69-39ca-a867-a2323533c1cc | -3.82722 | -52.29691 | 2025-09-16 04:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85c0272f-8f95-3eb1-b009-5abc2def5fcb | -3.815 | -41.56965 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 56bd5529-be8d-3ba4-85c7-b841297d383c | -4.25062 | -47.28435 | 2025-09-16 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 245c416e-062b-33dd-9459-cc0f24298205 | -5.79573 | -45.94127 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f490766-499a-3ea1-86d2-15a81a2bbd93 | -5.6687 | -45.05068 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8abc51f-28c0-3768-87f0-6a14c4d1be01 | -5.65516 | -45.80566 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54a36e53-6db5-31f1-abe8-8fcb92891dbf | -6.40444 | -42.65368 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 25a34b97-1dad-3e47-afa8-5b82746c8dc4 | -6.1674 | -41.17032 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a88bd7f5-564e-37cb-88a4-11abba90bdf8 | -5.79124 | -43.94247 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| cce56c1b-5f6e-34e2-ad91-4d9d76570183 | -3.07499 | -48.81205 | 2025-09-16 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3fbaa54-8add-3de9-b144-d02b8a8257a2 | -6.46104 | -46.01385 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ab2b582-b896-3210-b358-346a9e677742 | -7.67294 | -44.49567 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0f612320-29a9-3a6d-acb7-1c24ee49ba7e | -5.80275 | -44.86404 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f09acf99-6830-3ca1-a407-332730f29826 | -5.30947 | -45.03178 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 737eb26f-4f4f-39b6-9609-5e11e192cd36 | -6.18804 | -45.12423 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ffbe889-c44b-3e48-8808-6ff017330958 | -5.74888 | -43.93287 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96193068-d3e5-35fb-92dc-88bdbbf96734 | -6.40377 | -42.65803 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 64c40117-5451-334e-8fc0-1e5291feaf77 | -5.98453 | -45.79633 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3e2b2fc-7889-3e11-9ecf-5a2f70a43268 | -6.68211 | -46.3089 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 6a00a3ba-7c3b-3229-b314-93ec79f17899 | -5.92527 | -45.82622 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4145a59e-d588-308c-8d18-fa15537918d4 | -5.97906 | -45.8311 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7bc2c540-e5c1-3dae-b7cf-078064e25548 | -3.07865 | -48.81265 | 2025-09-16 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61e41d71-4b67-3103-a293-6d028916403f | -6.52397 | -51.19089 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddf875d1-11ff-38cd-aa26-120ef27f0a9e | -5.34151 | -44.82598 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 06020e45-50d6-3da6-93dd-70194e261f9b | -6.52719 | -41.82784 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0bfa6392-4030-3689-93e4-6dc4d09101f5 | -5.80069 | -45.93144 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README36.md)
