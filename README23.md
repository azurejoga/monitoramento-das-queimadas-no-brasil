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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2aeee5b9-8df8-31a6-97c2-b7d4cd21be7c | -14.2121 | -57.4098 | 2025-06-14 05:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 44184a0c-46fb-3ab5-9756-58d81d2ca6d2 | -13.887 | -54.6106 | 2025-06-14 05:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 43.4 |
| e1532a2c-86a6-360a-b4c2-15fb0a5c60d8 | -6.9602 | -42.9052 | 2025-06-14 05:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 223f2379-3f4d-3aa5-ad1e-18e8541f6d0b | -10.9355 | -56.8322 | 2025-06-14 05:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3fc43d23-76d3-3dfb-b83b-f70ed20ff64e | -10.9355 | -56.8322 | 2025-06-14 05:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| fd5eacea-4c9c-3795-9261-b8518614ca1e | -13.9062 | -54.6084 | 2025-06-14 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 6ca4d262-dfb0-363f-9c81-a86058d54e6d | -6.9605 | -42.8816 | 2025-06-14 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 97873fae-7b4e-3411-b58d-7efdbc017c88 | -14.2121 | -57.4098 | 2025-06-14 05:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 8c7cafe3-c9d3-3612-9282-517f9e9d009c | -6.9602 | -42.9052 | 2025-06-14 05:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| 43a0d182-e20e-3cec-9dc3-02d54fb0885c | -14.07304 | -53.40839 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 214efb16-5911-36fc-bb8f-7e2736c3def5 | -13.89299 | -54.61668 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 62ac7130-1c8c-30ff-90aa-d8695af8bbcc | -13.4989 | -55.66394 | 2025-06-14 05:31:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bb26770-4843-3978-81b8-f25a1e99ed65 | -10.86752 | -54.30544 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 628a83ba-f94f-3e19-abb1-e04a896a5117 | -10.93445 | -56.83368 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f177de49-470a-3985-8291-c8b7448471e4 | -11.00522 | -55.08582 | 2025-06-14 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0e0cd498-81b3-3500-a8cf-577555b70ea9 | -11.80166 | -57.34841 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee66db18-f568-3d85-860d-59dec6c8db7f | -10.29409 | -57.13807 | 2025-06-14 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bffdd37-415b-3bcb-ac4f-33f0ac1f4c5b | -10.92286 | -54.7807 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 95c30233-e4d2-342a-b6d9-fdfb2c91e32e | -13.89631 | -54.63467 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62a665ed-331f-3617-b968-d34aa9ebf957 | -10.92652 | -56.83038 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6e0b4613-6b22-3453-8378-1f9f2f6f1522 | -10.29039 | -60.55622 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68cfe439-400b-354a-87c7-5cbf75c99a2e | -11.80538 | -57.35328 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 243ac0dc-5341-312e-a1e9-66a27c23e776 | -9.66427 | -65.75208 | 2025-06-14 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a6894da-9408-31fe-8a51-d6a861aa75f3 | -12.68098 | -52.40109 | 2025-06-14 05:31:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 22802460-acfa-3a36-9467-2a2ae1d09252 | -10.29391 | -60.55676 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3e2d912-6f5a-3b44-be76-50c0afa89ad0 | -10.36671 | -57.22864 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bde66b4d-76fe-3ae9-9e90-214adf02b09d | -12.62178 | -57.89772 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fdca756c-214c-3138-85c5-90cd55a18e3c | -10.29802 | -60.55328 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14144cd5-e1af-3432-aa3e-beb277c148dd | -10.07475 | -52.74385 | 2025-06-14 05:31:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 30f3ec1e-f589-31f4-8b78-c910a2381a62 | -10.91768 | -56.82912 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe0d0e6a-5b22-3fcc-8b92-49fd43d608f1 | -10.92325 | -54.77773 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01fcf839-2f19-3e6e-b0cf-0422413b7336 | -12.61544 | -57.88084 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2778b49-bbf3-3de9-8208-b12830a9d72e | -13.89876 | -54.6138 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7187c168-01f9-35dd-ba04-1f5eeb1939dc | -11.81165 | -57.34787 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b330595-817a-356a-a8dd-f60d403544fa | -9.18167 | -61.86691 | 2025-06-14 05:31:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eea5ecd6-38f8-397c-a28d-ab2c0461be0f | -13.97291 | -54.45127 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0507711-904a-3d63-a4bf-0875ac6bae6a | -10.07439 | -52.74573 | 2025-06-14 05:31:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f366ac6-bc8c-38bb-8436-a5564f19eb65 | -12.68706 | -52.40194 | 2025-06-14 05:31:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a8effebe-5a5a-3c22-9c4f-7089e6c6220c | -10.87802 | -54.30685 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3408ef7f-3f19-3215-af20-5e2d633e89c3 | -10.92149 | -56.83407 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5a50ebb2-76a0-3aa7-824f-3e574870b78c | -13.9675 | -54.45042 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e92f738-5ec0-36bd-97c2-063092f5d54b | -10.04376 | -64.98151 | 2025-06-14 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39453776-4c30-3306-b012-ca14695bfc6f | -10.92176 | -56.82749 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68880695-57bd-37db-94e9-1401556dd662 | -10.86794 | -54.30217 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f004021-6247-3ad2-ab43-93c181692b7a | -13.58536 | -54.28476 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e631e96-4444-31b6-9f31-b3c3862ce1ee | -12.27741 | -57.26611 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 46b1e18b-506e-3186-b08e-d34f831fb0c1 | -10.94214 | -56.84347 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c3d1dc36-1a2f-32a7-96c8-792cbbc475b4 | -12.56828 | -57.75769 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43e8e40c-c9ef-3720-adf1-f6c80e2d49ff | -10.92089 | -56.83836 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 17362878-47eb-3f4b-acc1-b1a4557f100c | -12.28066 | -57.27523 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc088aba-bd51-379a-85fe-62e388701e3b | -10.56151 | -52.01211 | 2025-06-14 05:31:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0773b8b3-091e-32cb-8db7-756a4015b16e | -10.92502 | -56.83682 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 789ee6bf-4967-3d69-8640-c55c545fb061 | -11.56742 | -54.57081 | 2025-06-14 05:31:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6186b41b-3469-3003-bc46-ab14ba2c2824 | -12.50872 | -58.34347 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ad64bc6-a25f-3233-ba65-fb11e45cff9a | -13.89216 | -54.62368 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bda409bb-752b-33b4-a0e1-dcc167809b07 | -9.4 | -65.51125 | 2025-06-14 05:31:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2645ff63-8839-376d-9a3b-45746f2eec5d | -9.24582 | -63.28366 | 2025-06-14 05:31:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aba3903a-82ad-38c7-92d7-af2809cc43bc | -10.91528 | -56.84628 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b08b27e6-4fd3-3fb0-9d63-cce97ddc4e59 | -9.92031 | -59.90894 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86fade2e-5b03-3b0b-989a-56e12913d1e1 | -12.68152 | -52.39634 | 2025-06-14 05:31:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c5869950-431a-3f5d-bf1c-cd0875637b37 | -11.00947 | -55.09206 | 2025-06-14 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b9afe5cf-b3d7-3cdf-8962-113af893dced | -10.93828 | -56.83865 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2c5ee50d-329b-35ee-ac3a-213690890d55 | -10.93271 | -56.84668 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fce282ce-2fcc-3581-ac7b-7434d7c36193 | -13.8934 | -54.61318 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e34f53e1-e337-3b74-88c4-03a57571a311 | -10.8776 | -54.31009 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d14baf48-5fac-3439-b70b-84fcd34525ef | -9.88112 | -61.40508 | 2025-06-14 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c1a648d-5f65-372c-82dd-59f2f9f3b31c | -10.92618 | -56.82813 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a85d0de8-b9fd-339c-8f48-490879323c41 | -13.89835 | -54.61733 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| bca95b50-42b2-30a2-b343-a12f89a85416 | -9.92455 | -59.90533 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b78b2cb-84f2-3f71-a362-c1c1a70aa518 | -9.46536 | -57.85376 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6a9c2f6-9603-301f-9688-bec050cf1eed | -9.3889 | -57.52504 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b65474fc-93da-3cf4-bc33-14b465da5607 | -10.93386 | -56.83806 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 785a88f9-1cb6-37ba-80b4-fecb491437c8 | -12.61492 | -57.88477 | 2025-06-14 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a8d3cbc-5a6b-3ee5-8e7c-099ca1fc3973 | -11.80107 | -57.35263 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cf559468-601f-3ed7-9388-57b9e7144353 | -13.89794 | -54.62085 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4f04e747-49e3-3649-b4e0-7d6fdb9b98aa | -10.05297 | -59.35883 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c884d35d-a7d2-393e-a331-e478cff1aa40 | -10.27866 | -60.53818 | 2025-06-14 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5d2d40e7-6160-38fb-a122-8e9ad03fc42f | -10.60507 | -52.82775 | 2025-06-14 05:31:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7fe5bc3-23b1-3a04-8266-c2cd16355949 | -13.50068 | -53.48803 | 2025-06-14 05:31:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0038b47d-5776-3026-9223-f3838beedac9 | -10.92118 | -56.83185 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80fe1b75-513d-3cc7-9616-08a4d3f25934 | -9.46639 | -57.84672 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db3738df-8909-37f0-bb0b-5cd18546ac7f | -9.38837 | -57.52873 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 378190dd-789c-3fb9-b4a7-c0a5a0372220 | -10.86835 | -54.29892 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd7c8a3d-617d-3ed9-9246-a8fcc511fd1a | -10.92714 | -56.826 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fe378ae-cb14-39f5-be62-4dd92a434708 | -10.91648 | -56.83772 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11541a48-a91f-347e-bbcd-dc616550e09c | -11.9165 | -57.46645 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a40301aa-77a3-3d76-84ce-7b48083049b2 | -14.06818 | -53.39931 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 84d01c95-3226-32b2-b433-d880904f0e45 | -12.68761 | -52.39715 | 2025-06-14 05:31:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b4c9c58-fbe3-3e79-80b2-9dc9a594b9ac | -10.93713 | -56.84727 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fed9ff19-79bc-3dd2-9080-c6bb01b315da | -9.84485 | -63.66551 | 2025-06-14 05:31:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a203249-9d16-31ce-949f-6a5407b20d9c | -10.85516 | -53.78128 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71dbe838-f9c4-3d0d-9ff9-a5ae86252573 | -11.01021 | -55.08646 | 2025-06-14 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c6f65c3a-cac2-34d7-b7be-f537b361d000 | -13.58663 | -54.2841 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 344cceae-28ce-3ba9-8a53-1bb11f360a5a | -10.92364 | -54.77474 | 2025-06-14 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c6e74da-19a0-3fda-8744-1787e3082063 | -11.81521 | -54.50273 | 2025-06-14 05:31:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6c49cee3-bd48-3802-92fa-396742080e1c | -14.06866 | -53.39518 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a127b0c5-9a85-330e-b4dc-a819c7d3e2fd | -10.91588 | -56.842 | 2025-06-14 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 131acd8e-0355-345b-8faf-a1591164cd93 | -9.39302 | -57.52566 | 2025-06-14 05:31:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bbc29ab2-c0d2-3d7d-ae46-a635430bdc44 | -14.07932 | -53.405 | 2025-06-14 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0b13221-7978-368c-85a5-29ec2598ac51 | -11.80676 | -57.35151 | 2025-06-14 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README24.md)
