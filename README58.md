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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3deda813-0a81-3ec5-8d3c-9a11fd7df76a | -17.68668 | -44.51052 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e173c95-655e-3b38-9d70-dd335cbb63a5 | -20.53953 | -46.44282 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 3855954c-b7a7-338e-a251-2f11a47f0e57 | -12.80973 | -52.91219 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e48812e-d6a2-3cfa-a19a-525272413433 | -13.83969 | -46.25966 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 050ee06f-7753-30f3-b335-45d5a941e126 | -13.90772 | -54.00723 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf24a4e6-b325-389a-829d-6ab4eeb826f4 | -13.03917 | -48.04667 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7370720-08a8-3a38-82ec-23aeaa16af98 | -13.91039 | -54.01875 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98eb36b2-d7a2-3c0e-9c98-6af17e14c088 | -13.89546 | -53.99487 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22a43875-9c71-3ec9-9698-ec8b2245c24b | -17.37924 | -49.24132 | 2025-09-07 04:21:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fb25932-978e-3010-8f8f-15437fc3313e | -20.09529 | -45.32008 | 2025-09-07 04:21:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80d154b8-9480-3667-9ff4-e165eb6226a9 | -18.94742 | -43.70286 | 2025-09-07 04:21:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8119195b-51d9-37a3-b975-389133c2219b | -20.54348 | -46.43953 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fa7ee0f-d3ca-3e78-b0f2-7df75ed83228 | -18.9855 | -44.23162 | 2025-09-07 04:21:00 | NOAA-20 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1fdde93b-cf3b-3883-9ad4-e9c3b42d5510 | -14.49069 | -48.77241 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f44f52d-9d0b-3368-a253-8e3d105b8f96 | -18.99797 | -48.44375 | 2025-09-07 04:21:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c4f1cf8d-d39e-3a3b-997b-84b86b303cda | -15.83733 | -52.27303 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3a30877-7632-351c-9ea7-9f426e11e712 | -13.03148 | -48.07204 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a408ed9b-0a98-3a6e-aafa-c5e8316e0e04 | -14.27125 | -44.97664 | 2025-09-07 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa03f88f-1972-3e7d-92fd-b89d9b967d65 | -12.93279 | -48.03263 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a66892a-a2aa-314f-88db-6835a272b49a | -15.23333 | -52.37297 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4cb249d-752d-3fa9-9eec-1c79065ae47d | -14.48873 | -53.23916 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93d1f0ce-2377-3579-82da-c228eb5a6c4a | -14.49891 | -48.76585 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba843032-b9df-38b3-a811-b2f9d4123641 | -12.62146 | -56.98616 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e61b9333-cdd6-301a-ad0e-92cc01ed17c1 | -14.42451 | -60.19962 | 2025-09-07 04:21:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d935192-7591-3f7b-932a-f058d015de29 | -18.49647 | -49.51159 | 2025-09-07 04:21:00 | NOAA-20 | CACHOEIRA DOURADA | MINAS GERAIS | Brasil | 3109808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| aa171f2d-93a5-3ea5-87f0-815ab51b0af5 | -16.28305 | -58.12027 | 2025-09-07 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 669fc39d-a8bd-3ce0-ae70-cc14093e0a4e | -13.04443 | -48.07861 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e8d8866-b055-3906-b04b-3586bbc9ffd1 | -15.70241 | -53.56443 | 2025-09-07 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e474a61-5eee-3ef9-a751-201cdc816266 | -18.68977 | -44.45386 | 2025-09-07 04:21:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 035bb563-0271-357d-8a56-3a9957449f25 | -13.02678 | -48.07933 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98a7efcd-5885-3e68-bb8d-262cd7c353e7 | -17.68248 | -43.53493 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 78d9b036-3f8c-3206-a0fc-190679f3be29 | -15.84476 | -52.27829 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2d74da4b-ff30-3c43-b64f-eb50f40a0fbf | -14.564 | -49.1294 | 2025-09-07 04:21:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d114fe2-16e8-3c50-ab17-d465c5e9dd76 | -15.1406 | -52.35461 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 96ce586c-7c68-30a1-b4ab-b86e3109c2ab | -14.24008 | -53.37906 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a122b539-4710-3932-933f-a35ca3b52567 | -19.72271 | -43.92972 | 2025-09-07 04:21:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d61727c9-993d-3e88-b469-a11ebd396889 | -19.70013 | -44.87842 | 2025-09-07 04:21:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 68324178-4783-3b37-ab91-f1865c9e2c3e | -19.8812 | -45.02542 | 2025-09-07 04:21:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1af9723a-a5c0-3017-acd7-bcc375881b11 | -20.54688 | -46.44002 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6c91ad9-dbfa-3201-97a8-0738a9c7e49c | -13.84078 | -46.27436 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c915d3af-922c-398d-a29d-f7ce62ddc3ca | -18.03034 | -47.09254 | 2025-09-07 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a754ae2d-72e9-3748-b8e8-a9d934ab25f7 | -19.89351 | -41.43619 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b13c5753-46de-3a4a-9d02-eef3dadccf71 | -20.54292 | -46.44331 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 452557c6-5f74-3b6b-b98a-e4fa34762b51 | -12.4742 | -53.85997 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 235e0e3e-5076-3a2a-93ef-35382e736796 | -13.83802 | -46.27028 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bb0880c-901d-3950-a90c-9ef292e683b6 | -14.56534 | -49.12151 | 2025-09-07 04:21:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 578baee3-7b85-3570-96af-0c04ebb1f457 | -13.82643 | -46.27929 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dbfae39-2bdd-3d77-95cb-c1529b2a86e8 | -14.58738 | -52.14694 | 2025-09-07 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5baa6c54-e917-304f-bcc7-6dd2f492ce76 | -15.83503 | -52.28535 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 410ded4e-14ce-3cf1-9afc-5bd7d2fc3124 | -13.91472 | -48.03555 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8535d816-8a85-3196-a207-2ce5660db51f | -16.90463 | -45.74508 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c388122c-7c93-3ec9-8295-3dd4bdddc512 | -13.03176 | -48.04913 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe3e7a63-ff6c-3bb7-a906-5bd6353d6935 | -16.28018 | -45.68478 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8c7faa53-159b-3741-b40f-f67e3858c9a6 | -15.18202 | -47.97263 | 2025-09-07 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 34d0275a-ab77-304a-8442-753e15f17de2 | -19.4095 | -44.31642 | 2025-09-07 04:21:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51dcf8e9-899b-308b-8cdf-b3652ba37e75 | -13.04656 | -47.1232 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 63b9b327-2da0-3212-8303-12204da778f5 | -14.59152 | -48.10006 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02b9a7f6-67c7-3d2a-8b5a-71895e4c64bd | -11.16243 | -59.16582 | 2025-09-07 04:21:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 508a891a-6a46-39e3-992c-cf05f2d500d4 | -16.93816 | -45.76176 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 253db850-d11b-3fa4-befa-f566c1958f4c | -16.28691 | -45.68587 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3de122bf-eb45-3a22-8401-795946ea8721 | -15.36372 | -43.6643 | 2025-09-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1b47ca36-8df7-37e7-b1af-df0730466e42 | -15.23747 | -52.37372 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c649475-a51d-35e7-aaf3-a6b248ec98c3 | -14.97259 | -47.59275 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 697cdab1-5193-37f5-999c-0499de1e9bcf | -19.53525 | -41.54175 | 2025-09-07 04:21:00 | NOAA-20 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0b462da9-70fc-3331-876a-01dc098c5f6a | -13.84798 | -46.25012 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45963d1a-ab84-3065-8eea-7c2b2d59aa66 | -16.81936 | -49.18731 | 2025-09-07 04:21:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| deeb9280-ff11-38ab-8c4e-6f3bf566ff9d | -13.83582 | -46.26266 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e4987cd1-3f1c-3cab-bd29-e10966f2be35 | -15.53636 | -48.37878 | 2025-09-07 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8366d0b8-d39e-315b-85bc-4f98c165d1dc | -12.93751 | -54.77694 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0dd61268-5f3e-37b1-8c1b-1fda48b79cf1 | -19.58459 | -47.39961 | 2025-09-07 04:21:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bb092dc-e5ba-3ad2-ba01-24bd6ce92957 | -15.7007 | -53.56622 | 2025-09-07 04:21:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96e0836f-03b5-372c-856b-f8a80b28edd6 | -15.53595 | -48.37545 | 2025-09-07 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32c451a2-93f2-30f1-9770-379c83b7385b | -19.50727 | -42.57033 | 2025-09-07 04:21:00 | NOAA-20 | IPATINGA | MINAS GERAIS | Brasil | 3131307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f3025607-362c-3744-92d0-9db8ae3d7727 | -17.70126 | -44.4844 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 351f0fc1-3fba-32ca-a433-a03f029dc2e9 | -14.48892 | -48.76857 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8cfba4b6-c5ac-3ac4-a98c-45c737adf940 | -14.56818 | -49.12595 | 2025-09-07 04:21:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 20d816b4-5185-31a4-b976-9a358d1e84cc | -20.53218 | -46.44561 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| c02f66ec-49c5-328c-ad07-97546202cc99 | -15.84029 | -52.30235 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46eb270b-e914-3145-8e1e-3192551c0b2d | -12.93417 | -54.76702 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8fcece86-2a88-3033-8afa-b05ab3367d6a | -20.54916 | -46.448 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c317b054-107f-3b4f-b23a-2d9cb5ebbeb4 | -17.6781 | -43.53907 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6cdd5371-3740-30a0-aa61-9598f5bea589 | -13.93758 | -54.02982 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c23409a2-ee68-3d90-a28e-933d48504f0a | -13.82865 | -46.26514 | 2025-09-07 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33baabcc-628b-3958-a60b-bc607ad35b8e | -16.33397 | -52.94596 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 477ed800-57bd-30ce-bea6-9e0d523f4e5e | -13.02403 | -48.07476 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0c1415e5-1334-3897-86dc-8f91204e62ba | -18.94902 | -43.7009 | 2025-09-07 04:21:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61b035e3-879b-331b-813b-658ea167467a | -15.52386 | -51.72161 | 2025-09-07 04:21:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7c0695b4-45a2-38c7-8149-072ba4808b54 | -13.82918 | -46.28337 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 35b2ed12-1c83-3b66-b73a-af7fb312919d | -13.83747 | -46.27383 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd1db3ae-0419-3e2e-b8cb-f896c5be851b | -19.48374 | -47.76112 | 2025-09-07 04:21:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2178f8cb-9efb-357b-acd2-4328db295bf8 | -16.92483 | -45.77121 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c664675b-b9ac-331b-8d8f-1c869e1a212c | -16.5518 | -46.84578 | 2025-09-07 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15aba95d-2350-335c-9cca-4f67a9672068 | -13.05322 | -47.1243 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a55a9522-54a8-3c8b-bba0-e823ed7136d4 | -13.04713 | -47.11961 | 2025-09-07 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 133ad666-70ab-3e91-9165-94d69b0aee2e | -16.29824 | -45.69073 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2772b58e-1785-3465-96d2-ed4d0965edad | -15.17806 | -47.97574 | 2025-09-07 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90ebfde0-1e83-33cd-aa2d-55a2d3030431 | -12.94756 | -54.77901 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 631a5a98-2479-3ae5-899a-6fcad0160ac7 | -13.86177 | -46.24877 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a827880-1780-3ae9-a8f4-5401407b22f9 | -16.29488 | -45.69018 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f06fd95-9d71-3d84-ada7-b5f4ac4ff3b1 | -13.9386 | -54.02443 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README59.md)
