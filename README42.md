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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bc924b1-db64-3f6e-a782-de1e781abdb8 | -10.53981 | -50.43557 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 465232ab-d218-3d4a-8a8a-1c798514af70 | -10.49355 | -50.32473 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80168cb6-5694-3acc-9712-15162f4d5d30 | -14.57914 | -48.05342 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 857896d6-a15a-3a5b-b9ad-c49896cbcf58 | -13.49255 | -47.02324 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3950905-aa7f-3531-a000-772f6f4e20e0 | -14.79926 | -48.2213 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c147b4a-c19a-3ef6-8264-131bb86eb558 | -13.73102 | -46.92787 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37b357ae-211c-35f5-b3c9-ad6a424b9678 | -14.58112 | -48.04303 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 65f54b3c-1ddb-3305-8d34-c9794db0212c | -11.44479 | -47.29924 | 2025-09-03 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 968003dd-f650-3f3e-a7e3-2f94eda49e14 | -14.76514 | -48.13968 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c10f37e3-f2aa-3c56-b1de-530e9b83a097 | -14.0484 | -44.62617 | 2025-09-03 03:55:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8136cb1d-1bb5-3d42-b9dd-55a0e6e3e1c8 | -11.62864 | -52.07135 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96161555-f4b6-37b2-8c5e-364e485f5f9d | -13.6975 | -46.9586 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 961b8076-64b6-3313-9ef3-5eb4906d7105 | -12.99119 | -48.09259 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebe0ee49-302b-39aa-bba2-78905c800dea | -11.85881 | -52.42584 | 2025-09-03 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e98bf5c-46b6-3701-abcd-868732fbe8b7 | -9.13162 | -49.65731 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e4a4556f-ab95-3eb6-a4e1-30e210b47e49 | -11.26618 | -48.95271 | 2025-09-03 03:55:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eaffa33-d0b0-3405-bfad-50bbd0e2c7ab | -11.58754 | -52.10807 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 12b48102-2650-3d11-8e31-64d0ca94c804 | -14.80115 | -48.2113 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0083d6e-549f-372d-886c-3e9a5089cd3f | -15.01262 | -50.05667 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dc6787d0-32db-3675-8a16-ee3e303b59b1 | -13.90217 | -48.10872 | 2025-09-03 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd14fd13-5156-3d11-86aa-65706d41667a | -11.59474 | -52.13904 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8f7a379-f90f-3aa4-a3e0-71d7d38f07e7 | -14.18172 | -44.3168 | 2025-09-03 03:55:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36cf7433-5184-3790-b3f8-f8df6a3e830a | -15.90232 | -48.16676 | 2025-09-03 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 193d52bd-80dd-3db9-b2d4-8e4ce543fbf2 | -13.30168 | -46.82379 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44488bb3-dec1-3f2a-80e1-d67964f43d74 | -11.89546 | -46.66792 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 950eaa65-6ab7-3c1d-b503-83599e92d24c | -15.00192 | -50.05417 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 797a2999-5c90-3884-93a7-d85b1085182a | -10.54663 | -50.43233 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 464f6a35-c34d-3059-a4dd-7191a3ceaf64 | -13.2808 | -46.83628 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5428cefb-b483-322c-947f-a53932971355 | -13.90476 | -48.12149 | 2025-09-03 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbc246e1-8d38-3d43-8345-9a45fca7524e | -11.03035 | -45.06973 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d70c86ac-f1a4-3392-aded-878d58fb47aa | -10.91724 | -50.87293 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ea17021-76ed-3c48-9496-e4d3bd11c22c | -12.96403 | -48.07497 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d711440b-c0c8-36f1-ac2a-6979bfd3e683 | -11.05286 | -45.40773 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e989f42f-cbf0-3eb6-92c2-bf59aaed6bc8 | -14.63638 | -48.94198 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af399cab-3359-339f-acae-c6d406400973 | -15.20656 | -44.41411 | 2025-09-03 03:55:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e1bcd65-6446-3297-902f-cb395132ced0 | -9.63102 | -46.11979 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dbe9b539-0f9d-31fc-ac9c-3309a60018b9 | -10.94074 | -50.78352 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3e58994-5576-32c4-9aec-ad1ae1c0af54 | -15.15609 | -52.3597 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22ba55e2-beb0-3178-98bd-1da291afef4e | -12.51273 | -49.57824 | 2025-09-03 03:55:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7c40026-7e9c-380f-8311-d18a2682eaa7 | -13.53223 | -47.01208 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5060fc0e-6c2a-32f2-95f4-dc59f7b2f5e5 | -11.62257 | -52.13334 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c04ca0fb-70fa-3aa4-955d-58987579d688 | -11.38117 | -43.57013 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3d98378-ea64-33ec-9d81-6a5fb7f75dfe | -16.30137 | -45.68935 | 2025-09-03 03:55:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ec389e82-4203-3bbb-84fc-d959ebb82a33 | -11.11927 | -44.66615 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51f1b9c2-8a86-3baa-9f62-bcaa3071a938 | -14.77536 | -47.51421 | 2025-09-03 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c2dd128-532f-3d4c-8860-4eaffbf0e71d | -15.21358 | -49.7901 | 2025-09-03 03:55:00 | NOAA-20 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec5c0cd5-e20d-32e3-811f-09fc12487f67 | -13.27251 | -43.42723 | 2025-09-03 03:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f90e791-face-3f4b-9b8b-c4a1311ca1bb | -10.48769 | -50.33826 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a624436b-335a-3b80-a917-94ff46ea7d64 | -13.3106 | -46.82588 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4464249-dfca-33e7-83a0-d14993dedc00 | -14.99426 | -50.06425 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f68a21ea-72c4-3c0c-b532-b523cc6e5c5b | -14.9042 | -49.62604 | 2025-09-03 03:55:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8940092-5018-33fd-90f3-d36cccb6a61c | -9.70073 | -48.29964 | 2025-09-03 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22ce12b1-5fd6-37f6-b9d2-fb25dadd2420 | -10.14596 | -46.27246 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fc6fff8-6fea-3f33-95bb-7a49dc3363a8 | -11.59398 | -52.10955 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d5c40889-ca53-3e40-80ba-19b7a853359a | -15.21289 | -49.79354 | 2025-09-03 03:55:00 | NOAA-20 | RUBIATABA | GOIÁS | Brasil | 5218904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d7b6cca-c9fa-35cc-abaa-f2cf4c9537f0 | -13.87276 | -43.49287 | 2025-09-03 03:55:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7277892-adeb-3d36-8f43-1647362190b3 | -13.70194 | -46.88396 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aba8dff5-08d5-386b-937a-2fab1221f999 | -11.11098 | -44.64228 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26d01bc3-b443-3382-8cab-9ee187d83905 | -14.78771 | -48.17737 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79706842-3c8e-3a22-a4f6-03ee5bd87711 | -14.57431 | -48.05289 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e954f8b6-2c8d-3571-a91c-5bd3d6dc64b6 | -11.61262 | -52.14865 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5beceb77-4f47-3d49-8315-6859b8b77d0e | -14.96532 | -50.20594 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc89c95a-8795-34b7-ba41-41865b3f56ce | -16.40313 | -48.12842 | 2025-09-03 03:55:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32bd1e2c-983d-36b5-9c5c-ef9676123e57 | -9.63447 | -47.04244 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4307d62-6824-3b7a-90dc-7cf066946a65 | -12.8374 | -48.05493 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b156d786-094b-3608-9e17-5d96c00eb8dd | -13.72581 | -46.94075 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d7c1133-b1b5-3023-a496-080871af582c | -11.11843 | -44.6473 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2a5dede0-c4a3-3368-9108-6be836417ecd | -10.00497 | -46.90061 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 018819bd-4fd3-3b98-903a-6e941d9260e0 | -15.14956 | -52.36004 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fada715c-f755-3d77-9883-fb79ad3abe82 | -16.07784 | -43.62106 | 2025-09-03 03:55:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bafcbb8-815f-3166-9eeb-2e63d1f90414 | -13.88512 | -44.4538 | 2025-09-03 03:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 56fdcccc-469a-328b-a742-f955201ebe27 | -15.54561 | -48.32057 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 72690fb5-06c0-327c-8d46-8cb00ae770c1 | -13.49637 | -46.92158 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 022f2b6f-b852-37c8-a5c8-e9682ced5055 | -11.89634 | -46.66305 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34ef7579-8671-3bc1-b814-bce860dfe812 | -9.63036 | -47.85968 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ecdd024-c420-3a3f-9379-0b2f4a8fe497 | -11.04862 | -45.4069 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f8c5789-977a-38e0-ad80-2a0d684d1031 | -16.40891 | -45.65226 | 2025-09-03 03:55:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d6c3dd2-434c-33b2-9311-3ea58f6c4436 | -10.746 | -45.27436 | 2025-09-03 03:55:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fb8421f-65e5-3331-b77f-17b948c1e8ef | -14.97839 | -50.19734 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 597c28c6-52a8-3f48-97c3-325ff9e4ba37 | -12.18719 | -48.24884 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9ee3f2b-c214-3132-945b-196926e4914a | -11.8576 | -52.43176 | 2025-09-03 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 986335fa-e59e-3973-8089-aa2985c42b0a | -11.58411 | -52.12491 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 16e3e19d-57bf-3f79-905b-8e2f487caaa0 | -12.9963 | -48.11914 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7f8f703d-1158-38b2-bd62-c762ce7c57ba | -15.7564 | -46.87515 | 2025-09-03 03:55:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41e6f1b0-9d69-3dca-baf9-101abfed8a6d | -9.76429 | -46.9235 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1fa7ab97-f263-3be1-a5df-53c768752818 | -12.89147 | -48.0471 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f37cbda-a0d9-3b1c-b0f5-ea7039455f9e | -13.90113 | -48.11419 | 2025-09-03 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d933d7f-6bf0-3c01-8163-824a1c429932 | -13.50881 | -47.03668 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5d5e91eb-b650-3102-884e-7b23731e3fb5 | -13.30266 | -46.92693 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e849ba27-f9c6-31a4-bd85-9588c862cd75 | -10.14967 | -46.27819 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f8e5432e-fc9a-3a6d-aafb-6693662cae44 | -15.09358 | -48.12749 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 081abfad-58b2-3eb6-92ee-27e1352a3912 | -9.62922 | -47.86596 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d416b0c8-e5a7-334c-aa6f-b9ca3fcf4209 | -13.3171 | -46.82574 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38c3e41e-2395-3d00-bb1e-d91f48b72b8b | -13.52771 | -47.01115 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 671cc4d4-d50c-3dbf-a7d2-217f8435eb3e | -14.9966 | -50.05277 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa38ae36-9b66-3dd6-970e-9df65b4171ba | -14.79732 | -48.20528 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc1e2655-5ace-3814-8796-19f2071ae6c6 | -11.60817 | -52.07284 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3af4369c-8c49-3231-89fd-4c7840666f20 | -15.55611 | -48.418 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a8c9936-1f82-3984-bc78-9385ece930bd | -15.11978 | -48.17134 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 152d0ab6-4a7e-3462-a270-79a0b6942d1d | -14.58591 | -48.04379 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README43.md)
