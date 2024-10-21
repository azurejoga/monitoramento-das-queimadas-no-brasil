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
| 2237ad2d-0864-394c-b2a5-34534aff4355 | -10.20493 | -64.84101 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b990f71e-2b6c-3ae9-8a64-37d2431372b5 | -10.20432 | -64.84473 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cea54c88-e716-3c27-b7b2-118e4960eea6 | -10.20214 | -64.83673 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1cdf2239-82f0-31b0-b9ce-8e8d6a959296 | -10.20153 | -64.84045 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05a06f70-db62-37ed-85da-cf0d942f6ba5 | -10.20092 | -64.84418 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f162245c-638b-399e-ab31-6a94f29d3344 | -10.19873 | -64.83618 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ed7a729-e8f9-3154-9fef-979a432a3b12 | -10.19812 | -64.8399 | 2024-10-21 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d3fc7bf0-a77b-3516-930c-4b64af8f5372 | -17.00138 | -57.51969 | 2024-10-21 05:33:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 91d647d7-9aca-35f4-9b00-4565836400c7 | -18.29637 | -56.1732 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1cc47ba0-ab48-3c5c-a2c0-ebf7824642a5 | -21.3789 | -55.70701 | 2024-10-21 05:33:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2340590-2dac-3859-a7e6-cdfe38d49fd3 | -21.37858 | -55.71031 | 2024-10-21 05:33:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42e9d3e4-2d0e-366f-8e39-5c70c4971eb4 | -21.37826 | -55.71368 | 2024-10-21 05:33:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c237066-071e-32fc-ad60-97d662e20255 | -18.30144 | -56.17386 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 52b62cac-3c63-309c-a330-d8c1f5df4837 | -18.30109 | -56.17694 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1908aac7-448c-3ee7-902b-3741c648f6e6 | -18.29812 | -56.15779 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 5daecc65-bf33-33ca-bd99-3ba45e68d35a | -18.29777 | -56.16087 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8ea3b88c-3b2d-3079-818f-807c3b6d85c0 | -18.29742 | -56.16395 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d446c5f0-7e9a-300e-92a8-b6d7a2cebd33 | -18.29707 | -56.16704 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| eec6cbe8-5423-3847-8cdd-39f91b8d94d9 | -18.29672 | -56.17013 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 5f12b966-d6a7-37c3-9844-3a8e49d08e81 | -18.29603 | -56.17628 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| a40886ab-f72c-3410-97a1-9f94b3696a6c | -18.29568 | -56.17936 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 2f381002-c0d5-34fa-90b6-3e8c9f5a9883 | -18.29533 | -56.18244 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 3f44ac31-815e-31a3-b5a9-6d9e76a30fe0 | -18.29339 | -56.15407 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 03a593f5-6beb-3e97-ab2e-5c71689b9f08 | -18.29305 | -56.15715 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 441eaca3-2bfe-3f46-bcff-c6494a472b78 | -18.2927 | -56.16022 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cd81cf9d-15fa-30f6-859b-94dbda5aa273 | -18.29235 | -56.1633 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 09fd878c-e9a3-30de-bff8-e9a9ac658664 | -18.29201 | -56.16638 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b93020dc-cf7a-37f1-995d-59eb94c72fdf | -18.29131 | -56.17254 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 6d611b89-fb2b-32ce-b736-0b9ffe5ca55e | -18.28832 | -56.15341 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2fa8b829-766b-338f-9df8-c294938c6d01 | -18.28798 | -56.15649 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 76a04fd4-bdab-38c6-9be3-62a595756c82 | -18.28763 | -56.15957 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 759b4070-999d-3bca-abd9-873fd8b59b18 | -18.28001 | -56.08934 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 356266f7-3334-37e8-ad8e-227467666849 | -18.27966 | -56.09247 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| de7230c5-14ce-36fc-a098-64ff6ea8cd57 | -18.27932 | -56.09558 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 2d3f0f7e-4e55-37de-8078-045840977a07 | -18.27897 | -56.09871 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.6 |
| 3ad83d31-e5b1-3472-aaa5-ca4655dd6c1e | -18.27863 | -56.10182 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.6 |
| 610c45c3-0bdc-3f0e-9123-229b6ecce722 | -18.27828 | -56.10493 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 41.4 |
| 70dc1498-98be-3b07-aad3-8957d41832ff | -18.27492 | -56.08867 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d0e07de8-86d8-34f7-b95d-7628dfaa625b | -18.27458 | -56.09179 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 92c14fbe-6690-3e97-8b04-2c69d95f0995 | -18.27423 | -56.09491 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6cff7e06-fb1e-3fe2-b948-27977c901b72 | -18.27389 | -56.09802 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d186b87b-878c-3ac4-9af2-491005f093c0 | -18.27354 | -56.10114 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 01b2a6d1-bc67-32ac-990a-be592ca8e30c | -18.2732 | -56.10425 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 294d8b45-5964-320e-824f-1a71f89046c9 | -18.27052 | -56.08178 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 96df37a6-fec5-3e9a-89ca-f9f2e4b62f8a | -18.27018 | -56.08488 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8edbc231-4a5b-3086-833b-183c7da4d204 | -18.26949 | -56.09111 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 93e6bc97-a62f-3f2a-b363-6eb014015695 | -18.26474 | -56.08735 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b94ea145-42ad-3d0a-8d57-7cb479fb592a | -19.55819 | -56.61891 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| f89efc1e-0805-32b8-924c-40029a05dccb | -19.55803 | -56.61889 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f76bdb1f-9b7e-38f8-aa1e-6520689956b5 | -19.55735 | -56.62491 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8eabf047-df0a-3c28-9119-beeadd02916b | -19.55599 | -56.63693 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 818cae07-66bf-34de-aea0-411cbb7fcb1b | -19.55319 | -56.61827 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3c30b52b-cf5d-30f1-b079-5732a1159927 | -19.55304 | -56.61826 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d306e43b-4543-33cc-8718-6a20b86dcf7a | -19.55128 | -56.63634 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a8b64a6f-89ba-31a0-96ca-547a57015462 | -19.55065 | -56.64236 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e1076944-4015-3973-be24-78f585a6e70f | -19.55032 | -56.6423 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| ccf5d96c-df3b-3406-b619-c791b5d86c75 | -19.55001 | -56.64837 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b71c9e26-6a9a-347e-a4ab-a4cf4f998415 | -19.54964 | -56.64829 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3e2892eb-c276-31f5-9f63-9c71856e5234 | -19.54819 | -56.61762 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| da215e5c-7666-3a89-be3e-2fc28c1ce319 | -19.54804 | -56.61762 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 614f6215-2521-3487-81e4-265b4d5343e9 | -19.54566 | -56.64171 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 8d7ce774-c6a5-3ccf-b44e-62a8f110a2b8 | -19.54533 | -56.64166 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1a27fd9a-eaad-3a3a-bfb0-09b8a392efcc | -19.54502 | -56.64772 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 5b2877d5-4a54-3f47-90c7-7613ca57595c | -19.54465 | -56.64765 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 4c776928-6260-3ed4-82d6-07ec472575b6 | -19.54193 | -56.62903 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e55ada81-561a-3978-90df-b30911a60998 | -19.54169 | -56.62902 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| a10ba95e-5f77-3028-b1d3-aa5ca0f7a3f3 | -19.5413 | -56.63505 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d51f1097-803a-32a9-bec1-6dc4cd32d10a | -19.54102 | -56.63502 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 715aecf2-4877-3039-9e60-3565848039bf | -19.54067 | -56.64106 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 73a86957-6bee-319a-aa87-b2193b8b7350 | -19.54034 | -56.64103 | 2024-10-21 05:33:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7df192f0-cbec-38b5-9748-bd83593e89a8 | -18.04889 | -57.33826 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| e898a683-fb5f-3e92-8edb-bc15dd9c6d51 | -18.04828 | -57.34338 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 000b59e7-8b9c-3e63-bf7b-bf281f55f11d | -18.04361 | -57.34275 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 615ff924-8984-3ca8-b65d-21e758f360df | -18.01979 | -57.30312 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 109227c3-2fcf-39fc-bf07-d7dacc0d2463 | -18.01919 | -57.30827 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b65faebd-d18b-3b25-8401-709ce2a83f45 | -18.01511 | -57.30249 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a4f0ed73-a51a-3192-b6cf-081cd3aca678 | -18.01451 | -57.30763 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 328641f0-a8c3-3c72-8b56-834a7c4bef97 | -17.99499 | -57.43414 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 278c306e-e68f-3161-b70f-5310882f4032 | -17.93591 | -57.46563 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 82cc90c1-fe38-3158-9bf9-a64981b8525c | -17.92667 | -57.46437 | 2024-10-21 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 178c41c1-b551-3e62-8518-c88842ac1fd8 | -17.80313 | -57.48222 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9f38b695-caef-3de0-9786-3dce965309e1 | -17.79852 | -57.48159 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 5569128f-f5eb-3989-90e8-7f6422dad1b6 | -17.79792 | -57.48657 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d7fd7006-35d4-3bf4-978c-077afc1ba975 | -17.78871 | -57.48531 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1d79b03f-5a40-37f7-b0c7-32177035b601 | -17.77085 | -57.47784 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 213ea75e-acb8-3e19-a2c8-00a186677698 | -17.77027 | -57.48281 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 40bc7226-9700-31ad-ba74-5a1431db73af | -17.76555 | -57.56229 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b083ec7d-5939-3feb-91e0-bbaa124dc838 | -17.76497 | -57.56719 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d7031ed7-9811-374c-acfd-fb6e8e712c12 | -17.7334 | -57.47777 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7c508019-42ef-3a76-9f9e-78229d9727cd | -17.72963 | -57.47482 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 33c3ede5-e129-3c6d-b950-8e1cdc0ecd44 | -17.72879 | -57.47714 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2c52a2d7-7468-3e9c-9235-9cb1b399668c | -17.71762 | -57.45808 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 7dacba1c-02b2-3ec2-8266-a03f971edc7f | -17.71701 | -57.46306 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| db4916ca-153d-3948-81ec-9a712dfe4c36 | -17.71641 | -57.46801 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b49092e1-24bd-37b4-9a30-892a62728dc8 | -17.713 | -57.45747 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a2b8986a-8976-3768-b7df-ca00588a6d13 | -17.7124 | -57.46243 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 3453af43-5f4b-34b5-a08c-f13b720b65df | -17.7118 | -57.46739 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9fa5b7cf-2cef-3220-9a9b-c368ee8d5050 | -17.70899 | -57.45189 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9638786a-a417-39ad-bf3a-7a9651e5f2bc | -17.70839 | -57.45685 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| afa0f5d1-24b3-3c68-9d97-020e7f24e2bd | -17.70779 | -57.46181 | 2024-10-21 05:33:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |


[Clique aqui para ver as próximas entradas](README59.md)
