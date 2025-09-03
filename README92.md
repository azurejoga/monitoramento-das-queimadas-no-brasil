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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8171a081-b200-3cb3-aeb9-84a7f6467a0b | -11.85932 | -52.42991 | 2025-09-03 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85f6465c-8ce6-3b33-9728-8f8a8e7a6727 | -9.57384 | -55.39415 | 2025-09-03 05:14:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ce20ac9-9531-3651-a152-b04a10f7501b | -12.86422 | -48.02657 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc99e7e5-98e1-38ef-824c-0a23478d26d5 | -9.14282 | -49.64875 | 2025-09-03 05:14:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1f91bc5-1459-34cf-b9d9-89dce7bb4817 | -14.96758 | -50.20725 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44f26950-43cd-354e-bd0d-04a21e89671c | -13.73181 | -46.94204 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6922fcab-638d-3306-8f0a-de1f5cc9d067 | -12.44728 | -48.70976 | 2025-09-03 05:14:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d80cab1-f16a-332a-b4d6-5980e295cbc7 | -6.71938 | -59.78756 | 2025-09-03 05:14:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7e7e67d-10bd-3693-ad1b-2483236829d6 | -14.78514 | -48.15541 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5ba9b31-d6ed-328b-bc94-e7dfac897b11 | -11.80064 | -48.36314 | 2025-09-03 05:14:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ebfdb9e-2155-30c9-bf06-8b2f6aba1cb4 | -15.00537 | -50.05321 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81e82ffb-a7ab-3e8e-a7a2-a38f18f85bfb | -10.45754 | -54.77259 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f22faa0f-f3b9-3ab5-9829-0c52b4649bec | -12.48492 | -53.82871 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3996749d-fc15-3dcb-b5dc-49735cf8093c | -14.56231 | -49.14379 | 2025-09-03 05:14:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf10e95e-6db7-3bcf-8264-0e063e7815b1 | -8.8575 | -52.0205 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb8c08df-372f-3b53-acd8-21346d78ea7e | -15.0264 | -50.05836 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 549b7515-140b-3acb-ada4-e9939aec0067 | -9.05454 | -54.94965 | 2025-09-03 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 788784af-6e00-39c8-9b01-f41aebfefb8c | -11.26872 | -48.94518 | 2025-09-03 05:14:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8247f470-5694-3b33-8181-73ff47d534c9 | -14.60828 | -48.0172 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7e602bf-04e1-39c2-afc9-7502e1435f32 | -14.84027 | -46.69064 | 2025-09-03 05:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f9a2e281-4a80-35a3-b790-a4d014845e90 | -10.45351 | -53.61803 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e37134e9-5244-34c1-adc3-95549ca7c763 | -11.4228 | -55.18698 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e5f9c21-6e07-3fcd-8983-cc3f5c6df0d7 | -6.6775 | -58.86648 | 2025-09-03 05:14:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3668057-83d5-3174-934e-7aa2753219eb | -13.27838 | -46.83093 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25cd6c3e-7b0c-3f70-84f7-209e99d0319c | -11.60297 | -52.11269 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c7f87eb3-941e-30fd-bedd-a4687a5e6630 | -11.8576 | -51.53462 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c9c7425-1729-3f80-a8d5-20b6fc16e30b | -8.88117 | -45.82761 | 2025-09-03 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29a808ee-c6e4-3909-ba68-c4dc811e136f | -10.43117 | -54.77287 | 2025-09-03 05:14:00 | NPP-375D | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c68cc70a-8ba4-3750-8c9f-9ed552fc2d70 | -11.624 | -52.05791 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb0d44cb-ccb9-3c97-98b3-2adab8fef087 | -6.83474 | -59.36388 | 2025-09-03 05:14:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c55e1092-c264-38d1-9e76-ddbf93d11501 | -11.59354 | -52.11585 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 41401601-135c-33a2-9bad-017f4c606bb9 | -13.00118 | -48.11162 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30e09f17-a970-3f9f-9a4d-f0c7179a87c6 | -13.00954 | -48.09195 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4e1c8dd-66ee-3f31-bfb1-41e7e4a1aad9 | -15.01452 | -50.06761 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f8402a7-4190-3bd4-9c3a-85d3dc5e9802 | -9.65059 | -47.85726 | 2025-09-03 05:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b9e7b72-7550-35d3-9549-f2fce76031df | -8.36514 | -48.30827 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fd5a44e3-1075-39f2-952b-58bc91815b86 | -13.73267 | -46.93431 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 08838f6c-044c-3be3-b850-fa9bc725c8b0 | -12.6024 | -48.20255 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c38c8b71-b2cd-3b79-b77c-a0568e1dd093 | -8.86818 | -52.02879 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a36d4800-0baa-32e2-b738-f84771e70855 | -11.67402 | -52.18212 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88a7ab45-936f-39af-bb2a-a7dae665a603 | -12.49781 | -55.73876 | 2025-09-03 05:14:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bb145f3-bd59-31d8-bad5-78491d5237c3 | -11.47939 | -54.62395 | 2025-09-03 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f6a247d-fe78-3fe6-8de4-f94a9b99d161 | -10.55181 | -50.43143 | 2025-09-03 05:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c11a5b2-e4e5-3800-b30f-826f61c5e6e2 | -11.02972 | -45.06977 | 2025-09-03 05:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 481b52e6-3b2d-38e5-bcce-fca3bdb5ddb5 | -13.45194 | -46.92822 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fed70cf6-087a-3249-b9d7-3571a6c50e24 | -7.5368 | -61.33794 | 2025-09-03 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c88b1a45-2299-371d-bd6b-b17ca469f0e2 | -11.86557 | -51.54534 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71ae5fc8-854a-3c90-bbf5-e43af20d6c4f | -10.24452 | -61.76907 | 2025-09-03 05:14:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56335161-6ccf-3008-bbb1-b4de3464a466 | -15.00426 | -50.06293 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd4cf811-7116-30e5-91b8-e8c492e5392e | -11.58588 | -52.10598 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 609dd4b3-fd07-3c61-a992-a1a73c48ca78 | -14.97825 | -50.19638 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3b19052-094f-3683-888e-7697c3bf826d | -9.33595 | -55.23393 | 2025-09-03 05:14:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d18b3962-f0d4-3101-9afa-cbf4ab3f4099 | -14.56748 | -48.06415 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d04005c-a75b-3507-bf46-bf3c1fb8a08f | -14.76831 | -48.14274 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d448781-fcdf-37ee-ab2f-309bd35cd472 | -10.46064 | -53.62426 | 2025-09-03 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4fb9ec3-0eea-342a-a176-e49a65676574 | -11.62325 | -52.1288 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59e76e27-904b-3fb8-a2f5-5335be2a2724 | -11.61276 | -52.07402 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a809cbd-0c90-3c60-b9a5-6b7c660c118f | -11.81905 | -51.44798 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d54f4817-f857-3018-a408-586bb0918e28 | -8.3677 | -52.53653 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ced2330-e2a3-3307-afcb-5301b29b3c75 | -7.70285 | -50.29777 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d960e9ce-96e0-32e2-b78e-74fcea4062a7 | -13.10296 | -57.13765 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a2bcc39-b285-328c-81bd-450911ec6912 | -13.73311 | -46.93037 | 2025-09-03 05:14:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0dbae52b-18c9-37a8-9971-0b0b8a482a2e | -13.00166 | -48.10762 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d28e5e68-4c64-3b21-b4ff-a4d326073692 | -12.94758 | -56.99107 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d366b315-12fe-3403-8c13-79d2e05a54a2 | -11.64739 | -52.05223 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 211b5645-410e-3631-9181-e9006dd5854e | -11.61455 | -52.06096 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc872c50-40dd-3705-a059-f00a9544adc8 | -11.80426 | -50.64592 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| cfed6011-3361-324a-aa9c-ff47b07b5834 | -11.85988 | -52.42578 | 2025-09-03 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44ff42f8-37e6-3f04-9045-e95bc50f4671 | -10.97347 | -50.91037 | 2025-09-03 05:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aaf00be6-bf74-30d8-82c7-a57bf8a6bb30 | -12.91039 | -56.93499 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5d893865-ca71-3b04-977e-9e09a514ba24 | -11.60153 | -52.09023 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccb9cf64-1d18-3c2c-960f-916329214d51 | -11.81133 | -50.63008 | 2025-09-03 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa30f523-d326-308a-b46f-b0428e585df1 | -7.72464 | -50.24714 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 211da944-3e45-39de-a2a2-290a1e6e10a6 | -11.648 | -52.04782 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f16fb6aa-636d-3b34-bd85-45d3b532ce48 | -12.84195 | -48.06304 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2a98d693-245f-396d-a206-76968dea6c92 | -12.98723 | -54.75652 | 2025-09-03 05:14:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54588338-4d61-37ca-bd69-0b71f4e027a2 | -14.81103 | -48.21094 | 2025-09-03 05:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2425591-5283-3ba8-bbad-2b843ee9eabc | -9.81345 | -54.87938 | 2025-09-03 05:14:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c4c5201-a37d-30f0-89bc-4595f2e61eff | -12.92533 | -56.99914 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae5b2f5d-a89b-3028-915a-b43371a44dd4 | -9.6882 | -56.73975 | 2025-09-03 05:14:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b920008-666e-3fc2-bb73-0005ca99a952 | -12.92762 | -57.00718 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0f7a528-9b8a-33bf-b7a4-34e5e6c1f96d | -12.93842 | -56.9588 | 2025-09-03 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 293be4b8-778f-359b-a894-0501e0d9102c | -11.21283 | -55.07273 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f504df6-bcad-37af-8417-a1bdc97426f4 | -13.45097 | -46.92577 | 2025-09-03 05:14:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08186622-ed90-367f-b1b4-995877edfd3c | -11.19184 | -55.01226 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e4719a6-5374-342b-95a7-2b8b17695a26 | -11.4195 | -55.18316 | 2025-09-03 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b82e89d-e439-34ea-a9f0-8d51b1c7068e | -7.54054 | -61.33859 | 2025-09-03 05:14:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| fd0c50cf-28a8-3a37-a868-5a662270d080 | -12.89502 | -48.04704 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3e57de9-edc3-3417-8abf-57d9f4456f32 | -7.71437 | -50.25129 | 2025-09-03 05:14:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7abc7555-58bc-33be-8e1a-c479e44e304f | -15.10637 | -48.12159 | 2025-09-03 05:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc50dae9-a58a-396f-82a9-aacdaaee3455 | -8.36468 | -48.31168 | 2025-09-03 05:14:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc27b0a2-10ab-3621-bd52-5cc0450bcbfd | -11.61838 | -52.06597 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d33fae20-6e2b-35ee-a1e1-0890e26b3e72 | -12.4866 | -53.8329 | 2025-09-03 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7986db1a-81af-3315-9068-dececa9eae1d | -12.51266 | -49.57503 | 2025-09-03 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d651c82f-bea8-3666-93bb-28db5a639805 | -11.8543 | -51.41523 | 2025-09-03 05:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 92d3a43f-bd89-3f22-b59f-82c791a3ffae | -15.03356 | -50.04324 | 2025-09-03 05:14:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9969c90d-3af3-3577-972f-0e41bb296d2f | -12.29217 | -50.00876 | 2025-09-03 05:14:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10a67d8c-0b28-35e6-a036-e1d405ce2732 | -15.09816 | -48.12431 | 2025-09-03 05:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d1a9818-e3bb-32c0-9b99-347971b9dc68 | -11.64716 | -52.04542 | 2025-09-03 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dc7ae28-22b6-3c6c-8f5b-4f8d9925ca9a | -13.01449 | -48.10051 | 2025-09-03 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README93.md)
