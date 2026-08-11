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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74b0b7bf-6156-38da-adfa-95a95921e3a5 | -14.45141 | -45.68133 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae84cf38-e3b6-33a0-96b3-3dce7eade1c8 | -14.46035 | -45.70151 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a78ad005-d472-3f2f-9d17-351d982d5c91 | -14.12633 | -45.64473 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8b24b245-ef76-39bb-b7de-f9b23e8960e9 | -15.77513 | -46.78539 | 2026-08-11 05:12:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 487a39ae-8c94-361f-98d2-1507a2439546 | -18.01912 | -44.43743 | 2026-08-11 05:12:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3fd5b676-ba78-36a8-9fab-4d32ddc2ff70 | -15.03467 | -46.57986 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b82e8e3-b056-3dcb-8e39-d86ec8ea99c7 | -18.42828 | -45.49701 | 2026-08-11 05:12:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3815dbdc-3c82-34a1-b751-d1f828176d46 | -13.43622 | -57.05219 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 06f8d670-5a5a-35d3-8e50-5f6125cab9a7 | -14.27508 | -45.30713 | 2026-08-11 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa420e07-b848-359b-b3ff-3d11f77730ea | -14.40142 | -53.39439 | 2026-08-11 05:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f52dafa-f2b4-3b97-8082-b44e2af6d72a | -14.46222 | -45.68481 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 21543988-37fe-3f87-9a00-ea71792e4730 | -14.12681 | -45.64074 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b06e3292-9fbf-365c-beec-98efdc9a1ee4 | -13.43681 | -57.04856 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7f5cde0e-ab43-3045-9739-baa675bc1801 | -14.00289 | -53.97868 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0be4a04-c252-3436-8b5a-f283ee37f9c3 | -14.1253 | -54.00197 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63b89620-b540-3c90-8d61-dc4c565a3096 | -18.01232 | -44.374 | 2026-08-11 05:12:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67a480dd-86fc-3888-8126-06eae290f0ac | -16.48668 | -54.65592 | 2026-08-11 05:12:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb6de06f-3afc-3ddb-b57a-4136e16ffb0e | -14.6132 | -47.66213 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 546fceca-ef7d-3894-8909-bde279829f9f | -13.4307 | -57.04381 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86be69b3-98b3-32c2-93dc-7db3e1d98700 | -15.0132 | -46.57209 | 2026-08-11 05:12:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbe33d35-3aa5-3687-b297-d1af92658d75 | -13.42616 | -57.0505 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ac229b6-c3ee-34c3-be3f-d7d52505b5c4 | -17.1335 | -51.67963 | 2026-08-11 05:12:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60ae16f1-7205-322c-a2a2-a1a83616bd85 | -14.46661 | -45.69804 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 411f5480-8e43-3e92-962a-d6ad15191464 | -13.42675 | -57.04687 | 2026-08-11 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 102b5810-0431-35b5-b5cd-9e6aa1e9c91a | -13.82386 | -53.89661 | 2026-08-11 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 574f51dd-e02c-371e-9592-a89c6c92d86a | -13.63218 | -56.94797 | 2026-08-11 05:12:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b7d80f4-21ac-37f7-bec1-096b84fdf11f | -14.46615 | -45.70222 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 699edbff-ff8b-3d5f-8ab8-b3c983ef1421 | -14.45409 | -45.70497 | 2026-08-11 05:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2245d1d-3db4-3861-a56d-ed5c8078c00a | -14.38215 | -53.33393 | 2026-08-11 05:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8b8f314-98dc-3f62-a8a2-59484340fe87 | -21.46761 | -48.61164 | 2026-08-11 05:14:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98ca557e-7f0d-3a7e-8eb7-dc8a6485bdf5 | -21.46727 | -48.61496 | 2026-08-11 05:14:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47fdc6f6-a930-3e3a-ba21-26acdd46cdc8 | -14.6268 | -47.6506 | 2026-08-11 05:20:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| a4e061c2-28b5-370a-9550-b3fc12562571 | -4.2821 | -48.1791 | 2026-08-11 05:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2f2cf899-d50d-3c03-87fc-c3a2bb43f019 | -9.3909 | -47.4656 | 2026-08-11 05:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 43edf43e-d425-3bc2-a38b-dc5c31398610 | -9.3717 | -47.4897 | 2026-08-11 05:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| f42b6f11-0390-3195-8da0-6b3501d9dd05 | -9.3906 | -47.4878 | 2026-08-11 05:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 832688be-0239-3f98-a68c-acb8cd4cd04b | -9.3903 | -47.5099 | 2026-08-11 05:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 0c3db845-9d46-30e7-a8ea-c125c271f0aa | -9.3714 | -47.5119 | 2026-08-11 05:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 906c8a4c-01a5-3b3e-9127-316bce8e998f | -4.2635 | -48.1799 | 2026-08-11 05:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 4d778556-380b-395f-bdbc-3d38561b4c3e | 2.44664 | -59.93964 | 2026-08-11 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9426ad0f-9ba9-3c24-ba93-51735913bd93 | 1.64285 | -60.14075 | 2026-08-11 05:25:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92b87f98-17ea-34fe-9463-eb36d51a7e01 | 2.58276 | -60.04902 | 2026-08-11 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16292419-9773-38c5-8352-723b372546a6 | 2.44609 | -59.9361 | 2026-08-11 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 634b6966-0545-3630-81e0-86f2c74be5b2 | 2.44436 | -59.93988 | 2026-08-11 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71557a5e-e96f-3962-988d-2565d44faee7 | 2.38834 | -60.24021 | 2026-08-11 05:25:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33c8b42e-520c-36a5-a678-7efd0cd3ad7c | 2.58611 | -60.04844 | 2026-08-11 05:25:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3099137-5a30-36b3-8312-2fdca1a4f4eb | -2.95938 | -49.25732 | 2026-08-11 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d004ad4d-4657-3f3e-be6f-870affb239f5 | -2.09034 | -54.44572 | 2026-08-11 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 771a8677-7d8c-3db9-b40f-44ea517c221d | -4.26754 | -48.19209 | 2026-08-11 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| ca3dd661-186c-3028-91ba-8eb465d354a8 | -9.38537 | -47.45215 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a35177da-4b17-3135-813d-ba11d12caee3 | -8.66173 | -54.95792 | 2026-08-11 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0029c11-7599-3e19-a1e0-ee82601b77cd | -6.84027 | -56.41291 | 2026-08-11 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70b3a14b-74b9-324e-a5d0-a79aeb605fca | -7.39813 | -59.98774 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b60bad30-6539-328a-960c-5e572d20e731 | -7.39315 | -59.99778 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dae08ae-b071-310e-9f74-c3ac74008851 | -4.52822 | -49.2998 | 2026-08-11 05:27:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3dc6ae8d-01c0-3bc5-8b73-a9264af3b827 | -6.84341 | -56.41841 | 2026-08-11 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31cce627-ee22-34c5-ba67-dc7056b3b4f5 | -7.41259 | -60.00449 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 95e583e5-05f4-3df6-9219-74c6979da674 | -9.38836 | -47.48877 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 04ed8390-f118-3d1f-bd6c-7fea025359f5 | -9.39597 | -47.4601 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0eead966-b7f2-32a2-8be1-41b9dde2c3bd | -9.39169 | -47.46043 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| da2901aa-3c83-3fe7-8345-a0a56040fc72 | -2.95874 | -49.26163 | 2026-08-11 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9e6a4a1-88a0-3942-81a5-7362bbd44059 | -7.40593 | -60.00344 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a19ade11-52fa-30d1-9550-b3c5a0d60fd3 | -2.50607 | -51.81485 | 2026-08-11 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03c76c83-5af3-36a3-99ad-82218b0e436c | -6.01332 | -47.40409 | 2026-08-11 05:27:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0fc4dc34-24e6-3ad0-8214-7b51bacd1169 | -5.15336 | -62.54825 | 2026-08-11 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c1c7b2f-55e3-34d0-bb89-bcaae5716e92 | -2.91162 | -60.92476 | 2026-08-11 05:27:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9855f7f3-2bb8-3487-a246-ab9844c48ca8 | -9.38532 | -47.48727 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ffdb1e54-a2a2-3f44-af48-59ed489c17cb | -1.67831 | -55.23246 | 2026-08-11 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96d6f1aa-eb30-3d74-b374-c36abb9160c9 | -5.68857 | -60.23372 | 2026-08-11 05:27:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f873f38d-8494-3c59-9e89-7dbd2d81cbdf | -6.72019 | -58.93899 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 960a15af-953b-3aa1-b8ca-f1e51c93ac3b | -9.38256 | -47.45058 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| c65d203a-3a96-3db0-8da7-7fd0e01e3ad6 | -6.94972 | -56.43182 | 2026-08-11 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2b4aaadc-e092-38d9-8221-a21f98571d76 | -6.84883 | -59.10538 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aa26e427-686f-37ad-90e8-0abcc48f227d | -6.84317 | -59.09696 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c899cd72-f487-36a6-87e1-65c58d85b0af | -2.95744 | -49.27027 | 2026-08-11 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fed9f09f-aa54-324d-bc84-667195ecc4e9 | -7.40037 | -59.99532 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d951420-ba04-3517-a480-311c22aa79aa | -9.38034 | -47.49519 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8249df19-857f-3c11-b48b-1e9a709fa1d0 | -7.41037 | -59.99689 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0699c3d-8878-3813-8799-26e8975b3a50 | -4.707 | -56.01952 | 2026-08-11 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e0cfffe-c2e1-34b9-9a14-4de00cf8d1fd | -5.18462 | -62.56816 | 2026-08-11 05:27:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1500e3e-4224-3597-8f5c-44dd799d62be | -3.48715 | -50.05608 | 2026-08-11 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00f2e4ff-5836-362c-99cf-b68b05506650 | -9.38922 | -47.48147 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 41f7cefc-a5e3-364d-bc7b-d6db9470313b | -4.26185 | -48.18583 | 2026-08-11 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| bc792e97-a556-3c5c-a6e4-8a6222357702 | -3.17321 | -54.62128 | 2026-08-11 05:27:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 129ff6ed-f210-317a-95bb-adc965458eca | -7.41204 | -60.00801 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63842772-5c6f-33e7-a343-d404eefb9ace | -7.40758 | -59.99284 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63c34f92-ceae-3331-8af2-7170d4aacd51 | -3.37104 | -57.69796 | 2026-08-11 05:27:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d33837a-2b1d-3074-896b-5b9a74dcf999 | -4.26909 | -48.1813 | 2026-08-11 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 26ff08fc-0579-3caa-af92-e07c2aded005 | -6.84713 | -59.09381 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 085cc799-5bef-3938-92b9-cc7e0449c5ce | -3.61342 | -62.13557 | 2026-08-11 05:27:00 | NOAA-20 | CODAJÁS | AMAZONAS | Brasil | 1301308 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 455122b1-e92d-3e22-b347-45b05a3b2e4e | -6.84802 | -56.41405 | 2026-08-11 05:27:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c6b766a4-3c33-354d-bbe0-5f7dc2a47bbe | -9.39005 | -47.47442 | 2026-08-11 05:27:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1a55282d-7d81-3376-860e-80e0052f3c8b | -4.39515 | -50.96767 | 2026-08-11 05:27:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37469cc7-c838-3104-ad70-5e9032b8a4ab | -3.01033 | -49.55185 | 2026-08-11 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ae51fa7-f9d5-342b-b1a6-f2fd705a2f81 | -7.39703 | -59.99479 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f665f2df-ae28-3d7e-b136-fa546044804b | -3.54833 | -58.54405 | 2026-08-11 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b509e04-1c36-3807-a381-cc3e0e9b1bcf | -3.0045 | -49.55107 | 2026-08-11 05:27:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 049c3708-7586-3528-b966-af70f57522b4 | -4.52757 | -49.30436 | 2026-08-11 05:27:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acfc41e4-d75d-364b-8115-777f5df9c565 | -4.26832 | -48.18668 | 2026-08-11 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 3ea591c5-8768-3be7-a594-b7d6bfabd4b6 | -6.70764 | -58.95224 | 2026-08-11 05:27:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
