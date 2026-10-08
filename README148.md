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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3808e281-a94a-3e5e-bce6-5108e99b4bcb | -1.38757 | -55.43484 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9758d6cf-4877-3555-b339-4ac22705b737 | -3.00039 | -54.09375 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 895c5569-0d4d-3f47-a3d6-ed6ae9e60cba | -2.46797 | -56.0911 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06a98979-28a2-3d75-b21d-28850bf93a53 | -3.88935 | -55.8791 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ab11065-b731-3c3f-afe2-5d936289b199 | -3.01693 | -54.05662 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 620df2a1-5442-3b80-9b6a-1df51b658aa4 | -3.94589 | -49.01019 | 2026-10-08 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 618abb63-aca9-3d90-98f8-e82c8a42a88f | -2.74928 | -54.03711 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac43936b-ac8b-398a-9d9f-8339371042fb | -3.42911 | -50.43674 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70830338-b468-31e1-a70b-3051ade8824d | -4.2811 | -50.78574 | 2026-10-08 05:23:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7459a19e-ca39-3206-9a60-8b13b9e08def | -2.4713 | -56.09162 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fba473b-3b74-38c7-ab28-c01c12e0b5f2 | -2.47795 | -56.09266 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9b576c0f-9ed9-33bf-983a-b5355da8f916 | -4.37167 | -54.74649 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41e9c002-7465-3b0f-89ae-7c755fd9835b | -3.85267 | -55.9809 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1187985-76fc-3e3a-9d17-613f1b3af3f6 | -3.03135 | -54.10252 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 158cc0ca-d1af-301f-8926-7ee09c217101 | -5.24681 | -50.91792 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 168907c2-3708-350c-bcbd-0bbcffab53ac | -8.64765 | -67.18078 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| acc3381d-43d4-3ab1-bf16-04969aa71b1a | -2.56689 | -56.1702 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c62bf4c5-4a3a-335d-a71d-09613abe7ccf | -2.55853 | -56.43786 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f4f71d6-0036-39b2-a15b-e566f471c78e | -2.93795 | -54.16712 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a2ed7e8-e465-3b88-96f2-72304c50f461 | -3.86103 | -55.99296 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9da02d9b-41b1-3f31-803e-e06780b3097f | -7.4128 | -55.1676 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 969e5e30-ff80-32b0-8fca-2739aabb88cf | -1.36134 | -56.92083 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 846f56ef-29ab-369e-9117-33d6a850f3b9 | -3.53936 | -54.67128 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1907a6fc-28b2-3f0f-8c9c-1905590bf857 | -3.06875 | -54.25684 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2123af0-0119-3deb-b97c-e5e879caa300 | -2.64614 | -56.54783 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab85a84d-cc92-344a-bd06-b0ad9f306c5f | -11.32077 | -46.68667 | 2026-10-08 05:23:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| fb3423fe-b2e4-39b0-8ae0-10db1d58fce4 | -3.59045 | -54.3033 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65bd9e94-60fe-3961-8b32-7a6f760f2dfe | -6.14403 | -52.64701 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1083f58-b645-347e-9fad-2e00d936bd6f | -3.00961 | -54.12687 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 34b17666-4e03-3577-bbee-74e4fa917419 | -3.06109 | -54.20972 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09bec234-2000-30df-b15f-d1902d69c129 | -3.29697 | -54.08603 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45c5a033-d706-30ed-a405-8211076ed111 | -3.2591 | -54.67416 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c67e4289-67bf-3a85-888c-a0fc563a5236 | -3.71328 | -54.23473 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b6de8c1-29d7-31c6-9d39-3084a898ff31 | -2.96789 | -56.62991 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9699f4e5-6b96-3af2-98b5-243910733d90 | -6.17927 | -55.27304 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd3fad67-b0fd-3366-98b9-2b2247555d81 | -1.32111 | -56.40965 | 2026-10-08 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c27068da-581a-32f7-b755-2bd50efa0866 | -2.99032 | -54.13569 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6a2fdc3-3bb0-3c2b-be5b-a62b0a991dfa | -3.00671 | -54.12246 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9a3c5707-a08f-3a23-a416-427bc6b18744 | -4.93002 | -55.86013 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ebaf14ab-cf9d-3a67-952a-e3b2e4c9646f | -6.94839 | -45.29412 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 9c2e88c0-408a-35de-8b6d-e4032ca29961 | -5.98758 | -55.70305 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96f9ccf3-46c1-3b5d-b118-8b5b28bdab48 | -1.82902 | -55.04571 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb58c391-2c65-32f7-aeb6-a193cc783291 | -3.63629 | -60.6293 | 2026-10-08 05:23:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e781739-cab7-3726-a54e-394d7bd9201a | -3.02847 | -54.51741 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d785365a-4766-38dd-ab12-852600db75eb | -3.02876 | -53.91024 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb769611-0a84-38b1-93f5-2fe001f75f79 | -2.12212 | -54.80471 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| af95fb74-232f-39bd-8ab5-c0037dc63473 | -3.49971 | -51.68776 | 2026-10-08 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2a47d90-a3bb-3b3b-bcc8-bbb7e6efcd15 | -6.89124 | -43.69729 | 2026-10-08 05:23:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b9ead895-90ea-38ce-88a8-a9cf31d52261 | -3.1204 | -59.04227 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f2b6e6e0-4325-3ce5-a579-85880558a395 | -3.02083 | -54.10089 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 38f2b398-9177-3d50-980a-5feb41625c13 | -2.78732 | -54.0738 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7bb2bd43-1932-34d1-b04a-b808363742fc | -3.29044 | -54.01299 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bdd0f7ac-74ee-3bba-9c6f-559b3019fbe7 | -3.05152 | -53.95004 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3961c7b-d05b-3ee4-942a-d7b9100d16a9 | -2.48132 | -56.11445 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 107fc115-2936-3e40-a6aa-b7927c13288e | -2.94134 | -55.79187 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d2e41db-8200-35d3-ba69-bbfb6ede8c8f | -3.09221 | -53.94423 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a805ac16-3b17-3e77-abca-20b18c375b3a | -3.08559 | -53.96333 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 266a8f32-8edb-3a13-b8ae-6bdd51894605 | -3.29273 | -54.02135 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22ab07f6-7735-3936-9b4c-fede67103169 | -3.98424 | -56.21545 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b109d2c-22e2-3925-925c-5791e1c49dfd | -4.14938 | -54.91888 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad80ccc1-de83-3b0e-937c-8124153f85c2 | -2.87982 | -54.12662 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 172d8369-ca2d-365c-af79-80d41313115e | -3.43716 | -56.93447 | 2026-10-08 05:23:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 809cff99-9631-39c2-b11e-073ac6af10af | -1.82963 | -54.93263 | 2026-10-08 05:23:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d926d1ad-a786-383f-9c4c-b02738f8c5ec | -3.29837 | -54.05432 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b4d459a-55d6-36a0-bef6-ca107229673d | -1.52372 | -54.81259 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8775ef8-ca57-3267-ba1c-22effe5b9ce8 | -4.54102 | -59.92434 | 2026-10-08 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8bd638c7-a754-347d-a593-3dc9910e888c | -2.90299 | -54.02323 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b33c6a72-757c-3c3b-96eb-677f75510da2 | -3.14713 | -53.72334 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02b253ac-846f-3c15-812f-2c523915455c | -10.36556 | -57.73922 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 709bd1e0-7a8d-3039-9cd5-ca80f4aaff2b | -2.45356 | -56.37556 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82138a9a-5ce0-3cfd-868f-c84655abe25f | -3.2335 | -54.37508 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe5d8e49-4b96-3e47-a4c9-7168cbe64d8a | -11.34553 | -51.87122 | 2026-10-08 05:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4a19ef90-0553-3f73-9e37-e9fe2a62091c | -3.04508 | -53.94501 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a2a8021d-7ed8-3941-9c47-7358641cf8ac | -4.37661 | -55.16043 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86a4a04a-910c-3577-a8bd-ff8a8e0ff857 | -2.99368 | -54.18334 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27e1af90-a471-32ba-83cf-a614a7848006 | -2.76236 | -54.09053 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d855ed56-bf97-39f3-b500-a7c80f88c41e | -8.61313 | -67.02223 | 2026-10-08 05:23:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2a51f136-1742-3fcf-bd81-9c9162c99cd1 | -3.048 | -53.94949 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ab61119-65f6-395b-af50-2a13e11a4226 | -2.97505 | -54.11369 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 905cd55b-0ee5-3d76-8bb4-c9d035b138a5 | -5.23558 | -50.90356 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bdd1ef9-50c9-3400-a4ec-b74e6c53289e | -3.02165 | -54.04939 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 952f5c94-f891-3d00-b68e-b17b694039f7 | -6.03784 | -51.72751 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6498a8cd-d01d-324e-aa41-f286b03aa91c | -6.51079 | -55.38719 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad6e9ddb-f116-3379-adcb-c8222fd8cca5 | -3.54765 | -54.67966 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 9b57c0c6-2ebb-3b8c-9b75-6106b309bb04 | -3.86647 | -50.412 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 77a0e72a-6fc9-30aa-b013-327ea71a5bc2 | -11.9709 | -57.60823 | 2026-10-08 05:23:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74db035e-33a8-3d60-8d2e-8782c959d395 | -3.01281 | -54.05997 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 32f76ce8-bdf0-397f-b697-5db74836d95f | -1.47389 | -54.64291 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 182589e4-7965-3bb9-8e2c-0c6f15e580dc | -3.84822 | -55.98737 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d16b8f78-ceba-36f6-87c9-a6106f5660e2 | -2.84429 | -54.12209 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b179d261-4be6-30de-a56c-e3ba6c1d0cbf | -8.38943 | -46.30401 | 2026-10-08 05:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc69460a-89db-3a86-a514-9b59f6b5a426 | -3.61415 | -55.28061 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2568b433-6ae0-3749-8efb-0b61b842c4fc | -2.97678 | -54.03465 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0bc433c-156c-3588-a43e-d3f33d78d421 | -3.70666 | -58.93854 | 2026-10-08 05:23:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fead27e-1d2d-3fc8-889e-d5dae5dc3da8 | -2.49029 | -56.16545 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6930c2b-b11a-3ca1-a315-2b997767ed19 | -3.17506 | -50.45703 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5cb9ff14-8c65-33cd-bf79-f20fba58d70f | -2.99509 | -54.10481 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f3f8408-20e0-3968-a09b-ba545d44d86a | -3.20068 | -50.55621 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d1e3463c-a8cc-3834-91cc-16b9114f12aa | -3.08558 | -54.26341 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bd4babdf-233a-3107-8c00-be685963e2d6 | -4.15287 | -55.1409 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |


[Clique aqui para ver as próximas entradas](README149.md)
