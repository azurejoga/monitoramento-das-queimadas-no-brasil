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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90a86f25-1ba6-383d-a58d-3df8f24cf75b | -11.8158 | -46.5673 | 2026-09-15 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 33299888-8741-3c88-aa45-1c0480cb166b | -2.9579 | -50.3988 | 2026-09-15 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 14c96ba6-2a24-303f-a81b-3edd4b29ec71 | -7.0166 | -44.6184 | 2026-09-15 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 48050a63-21d3-3976-af28-c25b70d5faf3 | -6.5837 | -58.8498 | 2026-09-15 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 31487ef2-4de6-34d4-99c5-371590f1e31a | -9.7684 | -46.1293 | 2026-09-15 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.9 |
| d722c873-85a2-3983-a2e9-38d20c6760a1 | -13.2867 | -51.3046 | 2026-09-15 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| b317323e-41ff-365b-9366-4e0e9f356499 | -12.5333 | -47.1414 | 2026-09-15 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4363bf07-f563-3db8-b94b-f583079ab63e | -9.5496 | -51.3468 | 2026-09-15 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 9da4dacf-edaf-374d-bc65-0bee867185f3 | -9.4234 | -47.8588 | 2026-09-15 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ef2b8552-9295-330b-904c-2fddfd584a37 | -3.232 | -43.0224 | 2026-09-15 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b19fe783-98f8-3cc7-86b1-edb908315440 | -15.539 | -53.8502 | 2026-09-15 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 976524ba-2a32-388d-adf0-162f9525b9ac | -15.5199 | -53.8317 | 2026-09-15 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 8931adc4-c316-3517-8714-c41ca70d2ed0 | -10.6827 | -54.1679 | 2026-09-15 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d5dd9bc1-d10a-328e-a23a-4c9368ac6b5b | -10.7916 | -46.2298 | 2026-09-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 8712d8d1-681f-3e7c-a962-3a68729625d3 | -15.5397 | -53.8081 | 2026-09-15 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| de558e36-109e-3bbe-9d95-2e42838b0ee7 | -2.9025 | -50.4214 | 2026-09-15 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 118.8 |
| dec161ba-39a5-3336-a8ab-376100f55623 | -10.6829 | -54.1475 | 2026-09-15 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 9cd6c234-7cdd-3c9a-a8f3-90d0565246df | -6.8405 | -43.5254 | 2026-09-15 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 122.2 |
| bf2fad81-c052-331d-bdd0-7a7357812001 | -11.7962 | -46.5926 | 2026-09-15 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 164.5 |
| 4957a1c7-c7d9-3f6c-8c89-b0247954beed | -5.1256 | -55.9352 | 2026-09-15 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| a21bca64-72e5-3370-b86b-f9c9ff00cf8e | -2.6784 | -57.5504 | 2026-09-15 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 1edd802e-1deb-3a03-bd0d-abf9def7a986 | -9.475 | -45.4612 | 2026-09-15 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 147f622c-d632-34a7-9d1c-d2e34e44e671 | -15.5195 | -53.8527 | 2026-09-15 14:00:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 64.6 |
| a3c1dfa9-11c6-3021-96b9-7420d6578818 | -8.7949 | -46.9069 | 2026-09-15 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| c022921d-5a86-3f40-aa9a-94421034fd31 | -2.884 | -50.4219 | 2026-09-15 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 0f960c17-850f-31b5-82c4-e8b68ed6e21c | -13.3062 | -51.2808 | 2026-09-15 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 35ce80dd-eeb8-3665-99a4-5737846b0947 | -2.7768 | -49.4553 | 2026-09-15 14:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| db94b10a-03fc-350b-a7db-8c10e4ead23a | -5.1255 | -55.955 | 2026-09-15 14:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| ddba3aa1-9a4f-3547-befc-904b317da4a1 | -18.1709 | -51.7685 | 2026-09-15 14:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 99971c9e-4132-37b9-82aa-3615ea8bfa01 | -12.3277 | -47.9513 | 2026-09-15 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| c0252796-e814-38df-a684-38c355565c21 | -10.8855 | -46.3081 | 2026-09-15 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 356.0 |
| 923bcf76-ece3-358a-9a4c-a8329dcf8d38 | -9.4134 | -50.153 | 2026-09-15 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 70db67c1-b193-341f-a086-e9da03a12d6d | -7.0823 | -42.1107 | 2026-09-15 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 122.2 |
| b5ba755b-175e-372c-a948-0a00c581cb2a | -9.3577 | -50.0943 | 2026-09-15 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| d1792b7b-0612-37c9-bb42-14d651f722a5 | -15.0208 | -41.4621 | 2026-09-15 14:00:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 6e90b009-a9f3-3beb-b6f6-a1c8e501aef4 | -9.494 | -45.459 | 2026-09-15 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| ed0add15-c126-3be5-8fca-96dafeac3dfd | -13.287 | -51.2832 | 2026-09-15 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 257.9 |
| 9e45f667-fd57-39e6-a7c1-4c7c0f622c37 | -8.8137 | -46.905 | 2026-09-15 14:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 481193d6-6590-3d2b-b28d-057277d0aa96 | -15.2827 | -42.783 | 2026-09-15 14:00:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 8b60d225-dab2-3e67-acbf-bb192ebc1b38 | -6.8408 | -43.5021 | 2026-09-15 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 54e99fa6-8068-38df-bbcf-ff97be473728 | -10.792 | -46.2071 | 2026-09-15 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 4f4a2a25-98b3-3de1-8acd-43dd18ae6742 | -11.8154 | -46.5899 | 2026-09-15 14:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 9f1c2535-38ee-3ce6-a253-d2bdd528cbcf | -2.6602 | -57.5313 | 2026-09-15 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 142.3 |
| 4049c10e-d0e1-320b-8531-48dcfd7d7506 | -12.3085 | -47.9539 | 2026-09-15 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2d6c56c2-aea3-3f8a-b006-8608a5e58175 | -13.2678 | -51.2856 | 2026-09-15 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| d993fcfd-4f8a-3dcb-8f2a-a8cd5ec1bc9e | -10.8665 | -46.3105 | 2026-09-15 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 5dbe23ab-283a-38c1-8b62-2bec4390cf9e | -10.9305 | -48.3277 | 2026-09-15 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 0b24d32e-90f2-3296-9035-5f6762aeda6f | -8.5656 | -50.4407 | 2026-09-15 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c7dcc336-5d95-3847-a6d4-2be9eadca741 | -1.3007 | -49.1464 | 2026-09-15 14:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ff47e165-9666-32dc-93c2-dc8478e79132 | -13.3059 | -51.3022 | 2026-09-15 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 9d3d1967-d56e-37a2-9c5e-bc286b8fc224 | -13.414 | -57.0225 | 2026-09-15 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 9b9864a8-91d1-3739-8b30-a1357100532d | -2.9025 | -50.4004 | 2026-09-15 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| fb333365-5247-3bb5-b70b-d37cc6d884a8 | -14.1666 | -47.3876 | 2026-09-15 14:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 3742a6c3-06a0-3708-940a-b3b424a828b4 | -2.6601 | -57.5702 | 2026-09-15 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 1536dfee-e866-3936-86b2-8ab1e450c34f | -7.082 | -42.1346 | 2026-09-15 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| f3a32ac0-8f9e-31a4-b6ac-b15286c235c1 | -8.5468 | -50.4423 | 2026-09-15 14:00:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 01379b4a-7c39-344d-a465-b15621cb0e0b | -2.6601 | -57.5507 | 2026-09-15 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 156.3 |
| d9094e68-a686-39a2-8ad7-b2120987931b | -7.5608 | -62.33 | 2026-09-15 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| aabaa4c5-6dc9-3440-b178-e1e9ba9aeecf | -11.9168 | -49.7341 | 2026-09-15 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 9ce0b04f-25b9-3b51-b48c-28e25863ecae | -9.1337 | -65.844 | 2026-09-15 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 589b0223-73a8-3179-a3ac-61c1458d4a43 | -14.6779 | -48.0016 | 2026-09-15 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 68af548c-fe36-338c-a17b-afba6f130414 | -2.7149 | -57.608 | 2026-09-15 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 8e235318-1a7c-3526-8cf9-cb369bb7e904 | -6.8217 | -43.5271 | 2026-09-15 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6054f656-84ab-3b68-b57e-1c4943f66da8 | -10.2922 | -45.339 | 2026-09-15 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 13a56640-cc16-328f-bbf2-34d238ca23d4 | -13.2867 | -51.3046 | 2026-09-15 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| e1886aa6-c881-3099-85b2-b7d08751a19c | -11.5041 | -45.7939 | 2026-09-15 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 50fa0819-e0c3-32eb-9f26-c2a67e1a59ec | -10.2929 | -45.2932 | 2026-09-15 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ddf77bcb-104a-31e2-b1ec-121cc3cad26a | -8.7889 | -45.8999 | 2026-09-15 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 48c4cea7-62cb-3f42-a02f-ffcb40ac847a | -10.3116 | -45.3136 | 2026-09-15 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 160.7 |
| f76ddc73-c43e-32f9-bfca-8d4e4cc713b4 | -10.8665 | -46.3105 | 2026-09-15 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 9adc39b8-fe2b-38f4-a06d-cfc552370e31 | -6.8217 | -43.5271 | 2026-09-15 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 139.1 |
| 75069c05-642e-3f3d-be12-2e1cbaf2dbcc | -10.9873 | -49.6267 | 2026-09-15 14:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| aac9d669-b56d-32f9-b33b-de22de826de4 | -8.5656 | -50.4407 | 2026-09-15 14:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f83ea71e-2aee-3f0f-beb5-39f62c577d92 | -11.8154 | -46.5899 | 2026-09-15 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 173.4 |
| adf85596-7d6e-30d6-a1fb-dd2911d682df | -11.7962 | -46.5926 | 2026-09-15 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 223.7 |
| a95bb543-52fe-328b-99a3-fddd49d32e42 | -7.0823 | -42.1107 | 2026-09-15 14:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 136.8 |
| b57d778a-c2a3-352d-a569-a93e5ee1ce99 | -5.1255 | -55.955 | 2026-09-15 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 9e0fde7a-8d19-3f2c-a291-b43a1ee745f3 | -2.7768 | -49.4553 | 2026-09-15 14:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 6ee93716-4cc7-38bf-948b-597060da1f06 | -8.6191 | -44.4588 | 2026-09-15 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2f8ca825-88b5-3ba0-be5b-7d03647b5964 | -10.312 | -45.2907 | 2026-09-15 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 5d4e70a3-db3b-32d1-b663-2e96ebf5a7c8 | -8.043 | -43.7565 | 2026-09-15 14:10:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 616ff249-bbac-33f1-bc9d-40d2c9c57b4f | -12.3081 | -47.9761 | 2026-09-15 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 5c69d7e6-9628-3da7-92d5-8afb11c48434 | -12.6824 | -54.6968 | 2026-09-15 14:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b699e054-222d-3600-99c0-812701cfc6e2 | -13.2232 | -51.6744 | 2026-09-15 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 50902205-dc5e-3288-9fb4-a56b916829ca | -3.591 | -58.5384 | 2026-09-15 14:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 6ccf39ef-5662-3d4f-aa4a-2a3174fbdb95 | -9.1337 | -65.844 | 2026-09-15 14:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 60c542f8-d404-3f4e-9bce-f9de1cb6be6b | -14.6779 | -48.0016 | 2026-09-15 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| c00b192a-cdd5-36c3-b21d-37ac4566c83c | -9.494 | -45.459 | 2026-09-15 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 4cd308a1-ecd3-30bb-a8b5-e5f1ea94d31c | -11.8158 | -46.5673 | 2026-09-15 14:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| bfd00ed0-6fb8-3a2a-91c4-4d77aa9fd507 | -15.0208 | -41.4621 | 2026-09-15 14:10:00 | GOES-19 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 107.4 |
| 9140ab03-d43b-371e-9297-ad79d2f6c486 | -10.3109 | -45.3595 | 2026-09-15 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 382.3 |
| b8c3bb9e-be1c-37f2-bd61-4086bade03d6 | -10.6404 | -48.7114 | 2026-09-15 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 39.0 |
| c8002a0c-933e-398b-b22d-c5176f453467 | -7.1711 | -44.2367 | 2026-09-15 14:10:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 6a1c93fe-f78a-319a-a61b-d4f1455ffcce | -14.1666 | -47.3876 | 2026-09-15 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 102.4 |
| cfb4af65-b932-35a7-956e-28522c257e7f | -10.8855 | -46.3081 | 2026-09-15 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 350.8 |
| fd84278e-7c97-3203-b32d-a7d2d9ba2c13 | -8.2645 | -45.6378 | 2026-09-15 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| c353b386-7d87-32d3-bf60-4df450236f7c | -9.7358 | -47.0958 | 2026-09-15 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 4ae27a42-fde5-37df-a3d4-a3ff7d72b8e5 | -18.1714 | -51.7466 | 2026-09-15 14:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 8031755f-4a8d-3ce7-86dd-65e65c3ad4dd | -2.9579 | -50.3988 | 2026-09-15 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 858f16da-8daa-3755-a638-e29a2697de13 | -9.7687 | -46.1067 | 2026-09-15 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |


[Clique aqui para ver as próximas entradas](README79.md)
