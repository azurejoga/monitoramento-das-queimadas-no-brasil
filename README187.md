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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e293c267-af6d-35b5-993f-a422ceb30c53 | -10.572 | -57.4752 | 2026-08-31 18:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| cff51a07-38b0-35d5-aff1-adbf695ba1bb | -3.4002 | -61.3465 | 2026-08-31 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 790a95f6-d157-30a0-80fb-7e55f6108b07 | -7.6149 | -44.8833 | 2026-08-31 18:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 162.4 |
| e75514bf-9c00-384b-9f25-6ce16d5185d7 | -7.3302 | -60.589 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 95548fe6-b497-39ef-8aea-abf333aa3e04 | -15.712 | -39.8872 | 2026-08-31 18:40:00 | GOES-19 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 97.5 |
| 8e9f0fd0-9db4-3d25-ac34-ed4f441f6448 | -6.3844 | -55.2251 | 2026-08-31 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| edd0ad92-8a09-312b-b774-57c1822dfbd0 | -10.5644 | -46.1683 | 2026-08-31 18:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 207.2 |
| e27cd90b-2891-306e-981e-46d0f7fd090f | -7.2934 | -60.5713 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 20756920-92cc-3385-a62d-dc2ecec1f0de | -8.8521 | -66.7641 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 126.6 |
| d0e60d18-5812-3947-b349-0173979e30ea | -14.5871 | -54.0944 | 2026-08-31 18:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 39afabe6-7edb-3973-b0d0-b92a7b79ffd1 | -6.8991 | -55.7176 | 2026-08-31 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| a9cae43c-ebb4-3a78-a474-f33b409e5d05 | -15.8844 | -56.4819 | 2026-08-31 18:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 03811e0e-ecb6-3ce3-8ecd-99b4bff42ba0 | -9.1419 | -61.1027 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1d05b283-290b-3a58-81b4-4352dfc66dbf | -3.6399 | -60.5466 | 2026-08-31 18:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 3d4a4f2d-ef8f-374c-aaae-a7a168b28cf1 | -8.6673 | -62.8369 | 2026-08-31 18:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 8b22dde8-d378-39db-8550-9474aef287ba | -9.2092 | -51.5654 | 2026-08-31 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 297ca25d-8ac7-3af6-b97c-9bfd135ecbcb | -11.2286 | -45.1452 | 2026-08-31 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9cec0e81-77f7-3554-a6f6-85be9b74fd5f | -3.4979 | -59.0409 | 2026-08-31 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 386b0f61-dc86-3400-8f2d-42360cbc2f4b | -8.9481 | -62.3704 | 2026-08-31 18:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 13eb4b6d-9d56-3f14-8246-90aea5e19906 | -10.5451 | -46.1933 | 2026-08-31 18:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| cd54f68b-bac6-3003-a11f-97934435b57e | -9.0057 | -65.456 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| c69e4d57-67c9-353b-b161-fd3c506240e4 | -15.2669 | -53.8851 | 2026-08-31 18:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 94.0 |
| cc1f5948-8e07-322b-b422-3a36c71b93d7 | -9.1529 | -59.5609 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 58b9686a-50ae-31b6-8c9f-0015e7f1f6d5 | -8.6859 | -62.8172 | 2026-08-31 18:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 0533bcb3-7e0a-374d-afae-713141ba6fb5 | -4.9788 | -55.8417 | 2026-08-31 18:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 0dcb8149-ae5a-3957-bfdb-4ab0999e4f66 | -12.0929 | -44.9728 | 2026-08-31 18:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 6c1906fb-8580-3857-9401-6389407fcc54 | -9.9708 | -53.9419 | 2026-08-31 18:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| c6605ea0-0572-397d-80d0-fb4e03dab4da | -7.2933 | -60.5905 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 4981acea-811a-3705-a6c0-3ba663f296e9 | -9.4153 | -45.6726 | 2026-08-31 18:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 64cee286-4ad6-3ec1-a438-3ff574a4e965 | -5.4876 | -57.1416 | 2026-08-31 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 67d34182-864b-3f32-8e49-a486050b1335 | -8.9428 | -63.2797 | 2026-08-31 18:40:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1867e32d-5207-3927-a306-3eb9d7c521ec | -3.4185 | -61.3461 | 2026-08-31 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| a5835f49-27ae-3f19-8ccd-71c4f9ba0873 | -14.2369 | -51.9498 | 2026-08-31 18:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 646070b4-f321-36a0-87d7-e1532b4083be | -12.9054 | -59.8857 | 2026-08-31 18:40:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ad27c94a-efe9-35b1-851b-9e5e0629c616 | -4.1516 | -60.6878 | 2026-08-31 18:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ec2fcb16-e06b-35fd-89b2-dd2d0dbb072f | -8.3785 | -70.8639 | 2026-08-31 18:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 1739ab13-8f6f-3af3-ab01-8bf6c6946849 | -9.862 | -64.9771 | 2026-08-31 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f5a1d695-d2a4-34ec-af35-0180352a1f67 | -6.7123 | -58.9412 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3269a44c-1b94-3458-9722-51079a61a039 | -11.1807 | -55.1024 | 2026-08-31 18:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 68a463ea-8e09-3f6a-bd84-b2ace8d5b1ec | -7.6251 | -55.2987 | 2026-08-31 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 262.4 |
| be52f069-5691-3342-af91-892149fd75ab | -6.8756 | -59.4171 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| e70e3448-4aac-3706-ad8b-5f4454414a1e | -8.9314 | -62.067 | 2026-08-31 18:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 25f06b4d-04c4-3a39-9d94-7d89c9304ac8 | -7.9425 | -44.2538 | 2026-08-31 18:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 161.4 |
| 0fafdd17-8251-30a3-bde4-f60bf243512f | -9.2277 | -51.5847 | 2026-08-31 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 4964f2c4-ee37-38fe-8bd6-dab6a9178ea1 | -6.8569 | -59.4564 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e9f9fb89-daed-326f-b32d-e581c5cfc748 | -6.1294 | -57.6833 | 2026-08-31 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| e2f9ab2e-93f6-3547-b0dc-547604410376 | -9.0612 | -65.4916 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 53f16ab3-e57e-3637-bf17-60411b74c52b | -8.4896 | -70.6243 | 2026-08-31 18:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 69.8 |
| c99d98da-44c3-3900-a4ff-6b0b91a707e4 | -8.0445 | -72.4209 | 2026-08-31 18:40:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5a263f69-306e-395d-b3dd-0d69a95fb814 | -9.8434 | -64.9777 | 2026-08-31 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4c7fc533-d2de-38bd-8ee0-73e56ed731c1 | -9.1895 | -59.6364 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 2350c5e6-f546-3f0f-a918-024d41c591eb | -5.9636 | -57.6704 | 2026-08-31 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 04d43a26-22d9-3545-b26d-5850ebbac68b | -7.3487 | -60.5883 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 423.6 |
| 305645a0-cbac-3fca-b841-9e13c6f83fc2 | -14.8316 | -55.7399 | 2026-08-31 18:40:00 | GOES-19 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 2eb58859-4e0a-3f70-83d4-52f2eab301f4 | -6.7885 | -55.6436 | 2026-08-31 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 4940e2a9-61fa-3e63-9a62-d85bf0f46fd4 | -9.1718 | -59.5211 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6f9d674e-04b3-3aa3-ac9a-fa636602b6f4 | -3.1998 | -61.161 | 2026-08-31 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 10459117-ac3b-386c-a6c6-62f4107b08bb | -15.8649 | -56.4841 | 2026-08-31 18:40:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 75bc16f0-447b-3336-a8c4-1f929373b5fa | -14.5623 | -52.0984 | 2026-08-31 18:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 6159f72e-260f-37a7-9dcf-f71df557697b | -2.6888 | -43.5785 | 2026-08-31 18:40:00 | GOES-19 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| cecbcbd9-8fb5-3bd1-91b2-9769edaa7230 | -7.917 | -61.3481 | 2026-08-31 18:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 708873ab-64fa-3cc0-a6e8-1cd1b6468d5a | -10.746 | -50.6386 | 2026-08-31 18:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 4ecb65ed-2f64-37af-8d32-d0c921f38eaf | -14.4201 | -52.5201 | 2026-08-31 18:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e7cd4711-9d37-3a99-b115-40ce1871d613 | -8.6674 | -62.8179 | 2026-08-31 18:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f61445cf-e8ea-3f85-ba5e-a0e76173f0c2 | -15.0244 | -48.1689 | 2026-08-31 18:40:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| fbaab8c6-4003-3b20-ad55-ef33c934e170 | -6.1295 | -57.6637 | 2026-08-31 18:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 7473fed4-2839-3416-b943-e27eb213d864 | -9.6939 | -65.1145 | 2026-08-31 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 124.8 |
| 789304c9-5bc7-34dd-a999-801a29c9e4af | -11.1809 | -55.0821 | 2026-08-31 18:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 85f3afcb-dbc7-3dc6-b9e1-68909dc9d7ad | -7.6152 | -44.8605 | 2026-08-31 18:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 0c22e9f2-a43b-3a2b-8235-998e3a11cf91 | -14.2373 | -51.9284 | 2026-08-31 18:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d0608481-6cea-3778-a903-fdb1ac2b826b | -4.1698 | -60.7064 | 2026-08-31 18:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 375719ae-1412-31b6-8e44-31ab4b81c6c9 | -3.6076 | -59.0769 | 2026-08-31 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 97c65dd1-ddde-39b3-883c-97a8bc50ef02 | -10.3205 | -49.9567 | 2026-08-31 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1a6c61eb-be46-353f-8caa-d34798403f04 | -10.1084 | -50.299 | 2026-08-31 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| a401bff9-e20a-37b4-a53a-36c4b1481987 | -10.7271 | -50.6405 | 2026-08-31 18:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 147.3 |
| f56b21d1-f831-3dfc-ab86-71ac6e97a1a8 | -9.2089 | -51.5863 | 2026-08-31 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 3a036230-4fb8-3dd4-9cba-0791dfdc9286 | -9.2086 | -59.5773 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| ee879f02-5bcb-3613-8d8a-2a051ed3dcba | -6.406 | -54.7637 | 2026-08-31 18:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 8ba5d64b-70e2-3d5f-8da1-776caab28448 | -9.8927 | -60.2752 | 2026-08-31 18:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 6d69eee7-7552-315f-8c9f-ecced54db7d2 | -3.4185 | -61.3273 | 2026-08-31 18:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c00fc084-1807-31fd-89e2-5e4fc250bda4 | -3.1083 | -61.2191 | 2026-08-31 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d16fa90e-653c-33aa-aed8-b40056dac6de | -11.2503 | -54.0146 | 2026-08-31 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| a13717a8-2b7a-3337-af72-8952a53203dc | -10.7407 | -54.0401 | 2026-08-31 18:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 214.2 |
| 9853bd24-8341-3bc1-9a4e-b3a780e4ea8a | -9.694 | -65.0958 | 2026-08-31 18:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.1 |
| e4fa0f64-5a04-3eae-9dba-1d51103c3ee5 | -6.8416 | -41.7272 | 2026-08-31 18:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 330.3 |
| 7c567b37-82fd-3829-9a9a-e0c7d9807d29 | -6.9177 | -55.6967 | 2026-08-31 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 3a8a390b-6abb-3978-b8ce-8ebffb135b2e | -3.1266 | -61.2 | 2026-08-31 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ae868b0a-73c7-383c-b6c0-b550c5418ce1 | -6.6542 | -59.426 | 2026-08-31 18:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| baa908e1-fe77-3b1f-95f8-de0741d18f50 | -7.1435 | -72.864 | 2026-08-31 18:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 58f33842-d88f-31b0-8eb7-aaf009f51d84 | -14.4394 | -52.5176 | 2026-08-31 18:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 21f6a158-56df-3023-b6ce-d25842725af6 | -12.1113 | -45.0163 | 2026-08-31 18:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 214a8537-a008-336b-b6ee-aa6472a5a8e8 | -6.77 | -55.6445 | 2026-08-31 18:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 7d2dda7d-a33f-3966-8be1-c001b08bf4f1 | -3.1083 | -61.238 | 2026-08-31 18:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 44.1 |
| b273cbed-9369-39e2-88e4-12763bd0ca16 | -11.6967 | -54.6081 | 2026-08-31 18:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| f9d41687-12cf-3c26-abdd-e0d4d6a194a3 | -8.8705 | -66.7822 | 2026-08-31 18:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 273.0 |
| 0b25d2be-383e-39c8-b3bc-5167e32ba66e | -9.153 | -59.5415 | 2026-08-31 18:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 58c62614-3e0d-3310-a115-6cbd6cbe0457 | -10.358 | -49.9742 | 2026-08-31 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8b6b55f6-c197-3568-ba49-972f3269975d | -11.2482 | -45.1194 | 2026-08-31 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 2a72a23a-4fcb-37d6-9b81-ee1b51d503cb | -12.0925 | -44.996 | 2026-08-31 18:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| e80b7f60-9570-31f4-9933-c0aa80bffbe3 | -10.9862 | -48.4088 | 2026-08-31 18:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |


[Clique aqui para ver as próximas entradas](README188.md)
