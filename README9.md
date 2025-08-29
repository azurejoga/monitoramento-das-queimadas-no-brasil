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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6433af2-6d95-3fca-a45e-22eb3858965a | -22.68214 | -46.84646 | 2025-08-29 00:48:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 20.8 |
| 16c1da6b-d824-3d83-8325-9c541c3affaa | -24.16274 | -49.57408 | 2025-08-29 00:48:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 848f9cac-856e-3370-aa23-da0d35d88a54 | -22.6727 | -46.84794 | 2025-08-29 00:48:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| bff9a268-6533-36fb-977f-1bde9a445db6 | -17.60093 | -46.69421 | 2025-08-29 00:48:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a0ad3c2b-5a8e-3a81-a469-e6074612ebfe | -22.67437 | -46.8588 | 2025-08-29 00:48:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| 0e55c59f-326c-37b2-a2de-01380758e02a | -19.16584 | -46.59446 | 2025-08-29 00:48:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| bf5e9a0a-c520-3dc8-ac9f-b9ef5f9aa95a | -17.53884 | -46.62051 | 2025-08-29 00:48:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 4aa2f68b-d07f-3617-98d4-49e679f664cd | -24.18055 | -49.57125 | 2025-08-29 00:48:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 99d5f1c5-a2dc-33cf-81b0-dfffa0fb9dbb | -24.17163 | -49.57263 | 2025-08-29 00:48:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 14dfe4bb-90d5-327c-b4c4-dd18b461a408 | -24.17033 | -49.56292 | 2025-08-29 00:48:00 | TERRA_M-M | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 71ae039d-05f5-335c-aef2-04616244fcfd | -22.66498 | -46.86062 | 2025-08-29 00:48:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| c194fa4a-4eb7-38b6-989b-10872dd18fc6 | -19.1639 | -46.58236 | 2025-08-29 00:48:00 | TERRA_M-M | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| af4987c9-793d-389e-88d0-bfe7e76a53b5 | -22.6633 | -46.84974 | 2025-08-29 00:48:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 78f1cf88-91eb-34b6-86fe-b6db275747aa | -17.35237 | -42.64779 | 2025-08-29 00:48:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 261.2 |
| 1eccd0f6-b704-3613-8ae7-a67f2b9305f8 | -17.34788 | -42.62273 | 2025-08-29 00:48:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 93d29108-b2fb-3484-bfbd-00456e1cd147 | -17.60207 | -46.68756 | 2025-08-29 00:48:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 214a0d80-a70b-3225-b0f0-47ec36537b70 | -17.54709 | -46.6059 | 2025-08-29 00:48:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 7c456b3b-4e3e-3e22-9c8a-7f903aeca3ae | -22.13645 | -46.68312 | 2025-08-29 00:48:00 | TERRA_M-M | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 4cc458af-e546-3bc3-8e21-dd034916ffa4 | -17.03886 | -45.88132 | 2025-08-29 00:48:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 474e1ecf-9afb-3fad-b096-4aa4cbb46db0 | -22.13468 | -46.67195 | 2025-08-29 00:48:00 | TERRA_M-M | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 97a19aad-e4c6-39fb-9509-3b2eaff47c64 | -17.35681 | -42.64148 | 2025-08-29 00:48:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e0c45651-4b83-3a49-a187-7c23c3fdbda3 | -22.68377 | -46.85708 | 2025-08-29 00:48:00 | TERRA_M-M | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 31.9 |
| 14443103-aaa9-348e-90e0-19352ca27ff4 | -17.05213 | -45.8937 | 2025-08-29 00:48:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 67be5f25-9426-3770-833e-c21a1789af2c | -17.54912 | -46.61868 | 2025-08-29 00:48:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 277e52a0-b60c-3ef5-9d2a-79aea93167c1 | -13.558 | -46.8745 | 2025-08-29 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c9148684-0156-315f-b90d-de777c751708 | -17.3435 | -42.6581 | 2025-08-29 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e2c923eb-80f5-3da6-b422-0d2e9a501ce5 | -11.3133 | -43.5718 | 2025-08-29 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| c80afa53-0b88-378f-92ff-204d2f3fe218 | -8.1944 | -61.3747 | 2025-08-29 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| c953fb2e-2e8c-33f4-894c-ba13849e3e1d | -5.6268 | -45.0025 | 2025-08-29 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 255.3 |
| 9a8e93b2-3709-3edb-8c80-1b4c451e407f | -22.6756 | -46.8439 | 2025-08-29 00:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 109.7 |
| 2c2450a6-2918-30ba-8aee-25b99368b6ec | -11.3325 | -43.5689 | 2025-08-29 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2f336bcb-e5d7-30c0-acaf-bdc0c65663a4 | -9.4263 | -47.6384 | 2025-08-29 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| bb84a30d-2568-36c9-8585-d2f22b02e38b | -7.0381 | -44.364 | 2025-08-29 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 4fc9b973-b094-39d8-b144-5483d85717e8 | -13.2031 | -45.2834 | 2025-08-29 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 214.8 |
| 38206d28-83fd-3848-8a73-674575c805fc | -8.8987 | -69.4425 | 2025-08-29 00:50:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 62b80fe4-f078-304c-85a9-f1e241d7b21b | -14.2555 | -58.5084 | 2025-08-29 00:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 1e696957-28e0-326c-b77d-c8f8ca0210d1 | -12.0976 | -44.717 | 2025-08-29 00:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 208af24e-eb01-3d3b-8864-075b9ec6ec95 | -17.3442 | -42.6333 | 2025-08-29 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 5848a5c4-b241-3a69-8538-f82a22882def | -6.5546 | -43.9221 | 2025-08-29 00:50:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 162.3 |
| b8b82652-9e3b-36b5-95e0-877416041809 | -10.3812 | -57.8245 | 2025-08-29 00:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| d959de3e-8629-3852-8236-2b5146a2da80 | -22.6966 | -46.8382 | 2025-08-29 00:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| 8b62a4ed-b310-34e1-9bda-fb6fbcd0cc83 | -13.2027 | -45.3066 | 2025-08-29 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 91a4a851-2052-3b30-b7ed-8d4040a76192 | -5.627 | -44.9797 | 2025-08-29 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| d9debb97-6215-3700-bea4-6acbfeee27fd | -13.1837 | -45.2865 | 2025-08-29 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 257.4 |
| 6b414b28-c70f-3534-84ff-7c35c9845146 | -9.4618 | -60.5682 | 2025-08-29 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 157.8 |
| f2c62dd8-5cf5-39a5-97fa-e1ddd3ea583d | -13.5386 | -46.8775 | 2025-08-29 00:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e3e381f4-52d5-3f45-97e7-fdc1a1d0bbb0 | -9.4449 | -47.6585 | 2025-08-29 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 80d1ff9d-532d-3dc3-b6a9-fd324f161171 | -3.4254 | -49.0517 | 2025-08-29 00:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 4af3ed83-b61b-3865-b132-67567360c820 | -6.7072 | -49.4774 | 2025-08-29 00:50:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| fbf995ab-c1f6-36cf-883b-e106b4b32bc0 | -17.3643 | -42.6284 | 2025-08-29 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1d1a31fd-e82b-3913-8470-075c4230c811 | -13.2036 | -45.2601 | 2025-08-29 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 7122d9c3-8b44-3d41-8dbf-a4369186cd60 | -10.3624 | -57.8258 | 2025-08-29 00:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 917d2479-cfe9-3895-b44c-b0c1b99567e5 | -22.6748 | -46.8681 | 2025-08-29 00:50:00 | GOES-19 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.7 |
| 2cdff586-ef78-395c-9cf5-76a7b2c41c13 | -5.6266 | -45.0252 | 2025-08-29 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| efac397d-c735-336c-b9db-1a6527487a4f | -13.1842 | -45.2633 | 2025-08-29 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| f1d65ae2-5fd4-3155-bf55-4fa7dac3acf2 | -9.2178 | -60.8689 | 2025-08-29 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 46eceb32-2f61-3cf6-9dc7-a96808c82e10 | -7.0569 | -44.3623 | 2025-08-29 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 11c69216-6e85-3e1d-811c-87a74d3bc4ae | -10.381 | -57.8443 | 2025-08-29 00:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 2e0f4bd4-e0b2-3b2d-a25c-71512e5609ff | -9.462 | -60.549 | 2025-08-29 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 313ee3de-bbda-3c36-b659-011d648f7187 | -6.5358 | -43.9237 | 2025-08-29 00:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 07461f30-92d8-3ae1-a655-f8dc82d6dc26 | -9.4452 | -47.6364 | 2025-08-29 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 157e33ac-6e64-344f-8805-a805d239345e | -5.6079 | -45.0265 | 2025-08-29 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 2e78c4d7-f318-3b74-9da7-e89caa97158b | -12.4344 | -63.9364 | 2025-08-29 00:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 79114908-3d8b-308f-bf06-97c24fc1a0a6 | -8.1758 | -61.3755 | 2025-08-29 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 846c0bcb-90eb-38b6-8622-dc9af31f7061 | -11.3329 | -43.5452 | 2025-08-29 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 1cf0e70b-799a-369e-b70a-dcd600b85f14 | -13.1833 | -45.3098 | 2025-08-29 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.9 |
| d227cfde-7474-3692-9247-831ea1ee51af | -10.0227 | -51.1135 | 2025-08-29 00:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 91aa4b30-b20d-3182-9ed3-d32cd9849450 | -6.7074 | -49.4561 | 2025-08-29 00:50:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| fade3e6b-a8e2-30dc-a1a1-1b3af0f38e97 | -12.0784 | -44.7199 | 2025-08-29 00:50:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 2d09b1c6-5c04-3cb0-a76f-2a566a0db1f6 | -12.4345 | -63.9173 | 2025-08-29 00:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 143.6 |
| 817378da-4b65-37f6-bb65-96da09d9bc4f | -9.426 | -47.6605 | 2025-08-29 00:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 269e0294-4403-36b7-88c0-183c39702cc6 | -5.6081 | -45.0038 | 2025-08-29 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 3e8ec904-6c16-3026-9bd5-c4853773bc9d | -8.176 | -61.3564 | 2025-08-29 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 0e581954-7b4e-3d12-bec3-6f5c5b915f19 | -10.3626 | -57.8061 | 2025-08-29 00:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9e1f5523-1bc3-3936-8eb9-d0a09da744ce | -9.4432 | -60.5692 | 2025-08-29 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 1d552897-e89f-3b86-a4c0-cdcf8bedd359 | -11.95076 | -44.8461 | 2025-08-29 00:50:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 29.6 |
| a535622d-5fad-34cd-b2fd-6cbe71eb3df1 | -11.95366 | -44.85217 | 2025-08-29 00:50:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| c901da37-2bf7-32f9-bc5e-3e0af69573e6 | -7.63436 | -46.54848 | 2025-08-29 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| c30dbb9e-5106-3383-8665-89a23be47af2 | -13.19246 | -45.27118 | 2025-08-29 00:50:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 2527d030-5f2b-347a-879b-9607d4785d45 | -13.23468 | -57.13384 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 82348f91-ec21-3a22-b40a-f8c9203c8e1e | -12.66638 | -48.18903 | 2025-08-29 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9380e6ac-b813-3ffd-b47a-e4802e4ec7ff | -13.50321 | -46.84915 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 008b3587-5130-3110-a0ee-40bb4c0be78b | -5.61572 | -45.00188 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 421.5 |
| d6ed05c0-a34e-3ff7-bc00-4da5a0210b7f | -14.29724 | -51.93741 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 32897b34-082f-392d-9d34-11809da4c5a6 | -11.21917 | -55.06364 | 2025-08-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 20.9 |
| e3c4d068-61c2-3fb6-bcf4-a68543cff253 | -6.54694 | -43.95229 | 2025-08-29 00:50:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| c007ebe4-1ef7-314a-a14f-287517e527f9 | -13.66155 | -46.91692 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c5999491-be9a-315f-b757-76fdffbf5a56 | -12.8278 | -48.10395 | 2025-08-29 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b57c0e8c-f6f7-3eac-b4cb-367a398f8efb | -7.72554 | -50.29833 | 2025-08-29 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 9c57d313-89f7-38b3-a5f1-e0c2525b15f8 | -11.0297 | -45.07544 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 6cfc30d7-0dd5-38c8-a619-6bbf65815c38 | -10.64526 | -48.64615 | 2025-08-29 00:50:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5ebd1d84-840c-334a-8128-920ce0b91c3a | -7.72403 | -50.28806 | 2025-08-29 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 59a16e1c-3672-3ddd-959b-7d7410c8c22c | -13.9986 | -46.34214 | 2025-08-29 00:50:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| b95b046a-7e5c-3b10-859f-6c08e1d203e1 | -13.45156 | -46.9654 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9b7914dc-3fdd-3ab5-8449-6ae703056833 | -9.22534 | -60.8881 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 70d09051-0f78-3bb8-9798-64674555c14b | -11.08574 | -44.77008 | 2025-08-29 00:50:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| b93054ae-4132-3688-93af-043a5d9018ef | -9.46252 | -60.58189 | 2025-08-29 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 93b5b20c-2ce2-391e-9b1a-eda18da5f041 | -14.2548 | -58.50607 | 2025-08-29 00:50:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| af4ef134-0870-390c-8655-64f718ae0b55 | -13.1707 | -50.58801 | 2025-08-29 00:50:00 | TERRA_M-M | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5c852dd8-e9f8-390a-b823-a429e66c417c | -12.93571 | -56.97282 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 30.9 |


[Clique aqui para ver as próximas entradas](README10.md)
