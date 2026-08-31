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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8c30ff4-b3bf-35ab-b9b2-4347896bd637 | -6.8554 | -59.459999 | 2026-08-31 00:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 79c3b23d-5a8d-30d8-8bc8-d9cdfb171e3f | -14.4663 | -52.195 | 2026-08-31 00:11:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 52f58eaa-b316-3d26-bf3b-32a540c6355f | -15.6615 | -45.930199 | 2026-08-31 00:11:00 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 69a8895d-fb29-35a7-9df0-97d98e8a7ac0 | -17.9907 | -44.313801 | 2026-08-31 00:11:00 | METOP-B | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa87a482-55f8-3169-a953-f14166d444de | -7.5188 | -55.314701 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87ec4d0d-05aa-3a16-8f11-6894bfbcd8f2 | -14.4399 | -52.515202 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b91a52c-259a-3c0e-85bf-6bae1836fc09 | -10.8174 | -50.694 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed6c51c3-2163-3d7e-a70a-64eb0b9ebf36 | -5.2585 | -55.877998 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af170dc7-499a-3a32-8bf8-c2a4bb731416 | -11.2194 | -45.130501 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e50faa7a-6feb-3354-8a2e-77f88c1949d1 | -4.8601 | -55.834099 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf6d4fbc-1b37-38bd-bd6f-fd6206369d39 | -14.2011 | -44.5942 | 2026-08-31 00:11:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef8fa075-66b4-367f-8c30-fc631f8b9be5 | -15.2424 | -53.880001 | 2026-08-31 00:11:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d11dc3cc-f9f2-3f4b-9357-ff0dffc7b4b1 | -12.0814 | -44.9771 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ddda154d-cb06-3a16-a08d-a16028f92d39 | -12.941 | -45.907299 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e2d09a1-6396-3dc7-bf0a-ecc5bec11d41 | -15.6091 | -56.395302 | 2026-08-31 00:11:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d02e7d80-f555-3cc8-ab9c-7623ca5345b4 | -9.4366 | -45.665298 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 03da18ac-63a3-3364-814e-1fc69e64acfb | -10.8158 | -50.686699 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb9e870-5d95-3d92-8c49-0f2d46120658 | -7.121 | -46.081501 | 2026-08-31 00:11:00 | METOP-B | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e2bdff7-a7fe-3ab3-98a2-2bb22e939305 | -9.1567 | -59.361301 | 2026-08-31 00:11:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 344d5ddb-9d47-3205-85af-19802afe4d18 | -10.7711 | -50.8582 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9172f69c-6eac-3c13-b970-993b72ce6e75 | -11.3342 | -45.179001 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 371cbe85-9327-31c2-bc59-b19b70c9779c | -11.0774 | -51.513901 | 2026-08-31 00:11:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3296dffe-2c05-3f71-87b8-ce14e340b93a | -18.2904 | -52.678001 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec0b05f1-f329-3d4d-b7a8-3be3254619ef | -13.36 | -46.914902 | 2026-08-31 00:11:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 78a269e6-ba32-3216-a865-163fe897952a | -1.3939 | -55.736401 | 2026-08-31 00:11:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1e1a704-ff1d-3433-be24-2de12d32a77e | -10.1269 | -45.7048 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc700f31-bcde-329e-87f1-bf40d8bc1cf8 | -18.278601 | -52.6689 | 2026-08-31 00:11:00 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 76d14863-dc4d-36ae-9146-2c61a3af3bed | -14.6045 | -54.097599 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57087516-8d6f-33ef-a0b6-792980ea55eb | -11.239 | -45.125801 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17bf2f1b-255c-3767-b11d-c632663901b1 | -10.0637 | -48.692699 | 2026-08-31 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46254b66-daae-351a-9d42-54886a2c8773 | -11.2172 | -45.121399 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 49dc1b3e-b4cd-3324-a9d9-a0e61fc0f15d | -12.1375 | -47.250999 | 2026-08-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 23d213ad-e456-3cb4-93bb-8405e74d2494 | -13.1947 | -44.0616 | 2026-08-31 00:11:00 | METOP-B | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a7c02e0-cb1b-373e-9339-fa651842e670 | -14.1945 | -52.863098 | 2026-08-31 00:11:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d41a6d3-0954-3540-a48d-2550cabc1745 | -13.3935 | -51.8041 | 2026-08-31 00:11:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce87a8d4-9a39-3bf5-95bf-cbb0ec92e2ae | -14.4644 | -52.185799 | 2026-08-31 00:11:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 03c6ea88-f0a4-3bf9-943d-f5f0dcbbd223 | -12.3857 | -46.448101 | 2026-08-31 00:11:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb3513d-7e89-324a-9903-63dde815f415 | -12.1159 | -45.035301 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da321e5e-095d-3624-b300-9dbc3299bf40 | -3.9681 | -55.642101 | 2026-08-31 00:11:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da553142-b92d-3a7e-8c00-0b52aaac69a1 | -6.9348 | -55.641201 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e07d6653-cd09-3940-a930-a26a856f7a1c | -11.2227 | -45.100899 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e8a5064-220f-3e39-88aa-d042e33b0ce6 | -11.2237 | -45.148602 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 952a6b17-c569-38c8-932b-ffb27e108ece | -9.663 | -50.8661 | 2026-08-31 00:11:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd4b3722-cc80-3b62-be8a-0fc2b2978c96 | -7.4945 | -55.296501 | 2026-08-31 00:11:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f0879b-e4d3-32f0-8a80-82571f5116bd | -14.5947 | -54.099701 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5139cfb3-3a85-3703-8bf1-e49b22b612f3 | -3.6186 | -60.519001 | 2026-08-31 00:11:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03dfacfc-718b-3b74-a5b9-bbf2c1e66b12 | -13.9349 | -54.411701 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| abab5366-597d-3807-adcc-0d201da1067e | -10.8435 | -45.373901 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 31b264c8-e164-312c-8ce3-47297ec6dbd3 | -4.9628 | -55.835499 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31c632ec-e297-3c64-a7af-7b1b64d40413 | -9.4268 | -45.667702 | 2026-08-31 00:11:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4d78dc26-5289-3683-8154-1f107d745725 | -14.395 | -52.5448 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8305fd3f-8023-3b38-acc4-2a263eac25e1 | -5.2536 | -55.902802 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f4d6324-574e-3519-b174-17a1bcf45d57 | -4.9554 | -55.848598 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd08c5bd-f00d-3878-b409-178bdb5f92d5 | -10.7338 | -47.967098 | 2026-08-31 00:11:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3522ed3-9af7-38a2-b3e1-d16d11f90149 | -9.6738 | -46.544998 | 2026-08-31 00:11:00 | METOP-B | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 362e43d8-81a6-3b6f-b01d-c3dcd943b9b1 | -5.8654 | -57.747002 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0031a43-5f65-377b-8ceb-cde8446b174e | -5.4871 | -57.1231 | 2026-08-31 00:11:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2bceec7-9d49-3548-89cb-7c91cfddb057 | -11.878 | -45.820702 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f5d873f-81e5-3898-a21e-a40c84950831 | -11.2108 | -45.094101 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 95b8576f-feb6-3dc9-bd1e-2d2ca3a7d6f1 | -5.9334 | -57.684399 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 217e7ee3-9cb2-36a6-a576-adab398be5e8 | -10.8414 | -45.365002 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1bddadf9-e7ab-3c92-9e64-95f2baf8950f | -5.5981 | -43.997002 | 2026-08-31 00:11:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0dec302-b055-352e-b4d8-cb1636930b9e | -1.3917 | -55.726601 | 2026-08-31 00:11:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1f50b50-dfa1-3594-bc96-a50810c1618e | -10.9953 | -49.680801 | 2026-08-31 00:11:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1803c0e-c0cc-30d6-8176-4f4987331252 | -10.0574 | -48.664799 | 2026-08-31 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2c71f72c-6de3-3944-a851-e5fdaaa0bae4 | -12.0866 | -45.0425 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 796ec8eb-9c92-33b1-b863-d3507e197460 | -8.0815 | -45.474701 | 2026-08-31 00:11:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a25fc6ed-9c6b-3833-92c3-a9a2ba319f02 | -6.8986 | -59.473301 | 2026-08-31 00:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9396f7ae-7499-3c3d-a760-ce41b669108a | -12.3972 | -46.453499 | 2026-08-31 00:11:00 | METOP-B | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 320e46e5-1fa6-3854-bff9-194aa1b9aec7 | -15.4275 | -52.708698 | 2026-08-31 00:11:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aef9c0d3-3650-3169-ac13-acbc329721e0 | -14.206 | -46.555698 | 2026-08-31 00:11:00 | METOP-B | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 265eabed-7000-3c2d-8f42-26e1703aac38 | -4.1526 | -60.692799 | 2026-08-31 00:11:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 843741bd-66c3-30b9-8aa9-17143facaaa8 | -18.566799 | -48.292801 | 2026-08-31 00:11:00 | METOP-B | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0575dba7-bea7-3689-ad34-cebcfd7e090e | -18.3111 | -43.230999 | 2026-08-31 00:11:00 | METOP-B | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c9aeedc-aca3-3739-9811-6ef58660f054 | -15.9075 | -56.210701 | 2026-08-31 00:11:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0a9db0b-5e9c-3dbe-a3fe-b5395372033e | -9.9296 | -60.481899 | 2026-08-31 00:11:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e4295ee-8677-3f65-b00f-2e6eb40e4938 | -4.6645 | -55.922798 | 2026-08-31 00:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0db8e772-1973-3d9c-8a4b-76ef232f80a5 | -6.4813 | -49.889801 | 2026-08-31 00:11:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c354349-ca22-3476-babd-547c7210b8a0 | -5.9529 | -57.680302 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ce80da8-b070-30ea-9e0c-e01231565d4d | -12.0983 | -47.260201 | 2026-08-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9dfc834e-39fb-352f-ab51-762add80b6e6 | -8.3771 | -45.765999 | 2026-08-31 00:11:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b4bd643-dab1-35df-b6b7-72349561aad5 | -10.1351 | -45.739601 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 78aa10ea-2445-3591-973e-9a970d8649a3 | -12.1489 | -47.256001 | 2026-08-31 00:11:00 | METOP-B | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 102bd9d0-4d70-30e1-8022-4364e318f1ae | -12.1007 | -45.058102 | 2026-08-31 00:11:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 491a0333-b720-30ca-b93a-54db7c7478e9 | -6.8873 | -50.412601 | 2026-08-31 00:11:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fddfbb4-c629-358d-b71e-2a4b21139a4f | -5.8687 | -57.762501 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2646912c-2e5e-3dcf-86fc-e135e8bebb1d | -14.3045 | -52.902699 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fbd1e259-0af0-38ac-a37d-7910c60d607f | -12.9177 | -45.895901 | 2026-08-31 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf14940f-408e-389f-a5b5-60ea4a6b4ac8 | -4.0085 | -48.937599 | 2026-08-31 00:11:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce674593-c9d3-3511-94fd-01e7acaf89a6 | -14.6021 | -54.085602 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e67e6e7-c023-32fb-bfc6-f39415eca2a7 | -15.9204 | -56.226299 | 2026-08-31 00:11:00 | METOP-B | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 580c73e9-8798-38b7-a0cc-d81356fb2418 | -10.811 | -50.664799 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| adb3d707-f54c-3027-85af-6112fc6569f1 | -11.3287 | -45.199299 | 2026-08-31 00:11:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56b9ab5b-84c3-3e40-b7a3-a94230f635eb | -10.0524 | -48.688099 | 2026-08-31 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b49eacaa-069a-31c3-b221-0904527bf290 | -13.9423 | -54.3974 | 2026-08-31 00:11:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7180bd94-45a7-3ca8-9cfc-1080d134341b | -10.7581 | -50.845699 | 2026-08-31 00:11:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 32627f76-a9da-31a3-a496-612850ffa6c7 | -14.3891 | -52.566101 | 2026-08-31 00:11:00 | METOP-B | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b89d267b-f3a3-355f-9bfb-9b3af4df5cdb | -5.5867 | -42.322899 | 2026-08-31 00:11:00 | METOP-B | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8763dd30-77d9-35d8-852c-4d6fde937abc | -7.142 | -46.171001 | 2026-08-31 00:11:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ded6a3c6-f2e4-3e6c-bd19-b49a9729b508 | -6.1547 | -57.767799 | 2026-08-31 00:11:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README3.md)
