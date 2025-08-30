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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27441fc8-6b3b-3004-8c11-c70e9f0ffbcf | -13.9923 | -44.5649 | 2025-08-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 3ac23abb-7ae8-39f5-a0f8-497376013671 | -14.8399 | -46.7532 | 2025-08-30 13:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 4e10b723-ab7a-3c2a-b919-e99a75dc5b75 | -11.7347 | -51.7618 | 2025-08-30 13:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 13f60622-1c57-3bb4-a03c-4fbfec83c387 | -9.4862 | -48.8346 | 2025-08-30 13:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| a6acb180-b459-3102-9d25-3aa5e613d905 | -6.7814 | -43.7865 | 2025-08-30 13:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 0dd10e8a-1715-31ab-9170-a1da197e4431 | -12.8605 | -48.1657 | 2025-08-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| b07173f1-22c1-3174-b3fc-ae8533718448 | -13.518 | -46.9486 | 2025-08-30 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| fb8d5936-ded6-36c3-a7f9-04417ac0ab43 | -7.8541 | -46.9747 | 2025-08-30 13:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 301.2 |
| 367b5f91-3206-3877-b993-9136d35e0116 | -14.0118 | -44.5614 | 2025-08-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 387.9 |
| a3ef473a-7e1b-3f51-8fd1-3ebb285e1d58 | -13.3628 | -46.9953 | 2025-08-30 13:20:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 551387ba-a446-3959-a639-0765b0e217eb | -6.1787 | -43.9995 | 2025-08-30 13:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| b50e74c5-9991-3314-be51-4c39e6e7cb35 | -9.4498 | -62.3294 | 2025-08-30 13:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 4c3e6702-7738-38ac-9fad-abc7abd23f72 | -14.0313 | -44.5578 | 2025-08-30 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 229.4 |
| cb2bf56e-1f97-365c-8f31-b1df92eff856 | -9.6758 | -65.0214 | 2025-08-30 13:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ce8892cc-2e78-3e58-99aa-39199ab57f83 | -12.6686 | -48.1704 | 2025-08-30 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 8c3fc17e-2fc6-3974-b655-a6f6cb05eb95 | -7.603 | -42.7232 | 2025-08-30 13:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 106.6 |
| 671e7914-4f66-3e88-a1b1-7c89f154c36a | -7.0951 | -44.3128 | 2025-08-30 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| a2e21024-4304-3542-b561-66a1d0be94d5 | -13.518 | -46.9486 | 2025-08-30 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 5dd36002-58f5-3a4e-b8bb-1d91ac585cd4 | -7.603 | -42.7232 | 2025-08-30 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 119.6 |
| bc0a3297-0d39-3c3f-8ef8-62570dad2442 | -6.7814 | -43.7865 | 2025-08-30 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| fcb03996-0532-3718-b16c-023c61ae0e16 | -11.3317 | -43.6162 | 2025-08-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 251.6 |
| 7b890ea4-9ad2-3111-9f1a-20727d7d4ca3 | -11.3321 | -43.5926 | 2025-08-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 9f3f151f-8560-3df6-8e61-84f765e41b1b | -7.8541 | -46.9747 | 2025-08-30 13:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 67a33e17-f8db-328d-ac79-960170de7a30 | -7.1108 | -44.587 | 2025-08-30 13:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d01f6a86-387c-30ab-ac97-c8cc9e411b5b | -7.5842 | -42.7251 | 2025-08-30 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 0b386e10-7ecb-32ad-9fb0-6bbe906bd719 | -13.3817 | -47.015 | 2025-08-30 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 7b6e5983-9d1b-3499-9971-852dcc19c73d | -6.1787 | -43.9995 | 2025-08-30 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| f14d9744-610f-3636-a940-994826527b83 | -11.312 | -43.6428 | 2025-08-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 332.3 |
| 81e74b46-7223-30af-b4f0-c5250a3d3231 | -12.8605 | -48.1657 | 2025-08-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 95bcfdba-ea58-30f7-9f5b-da7ae8dfdde9 | -9.4497 | -62.3485 | 2025-08-30 13:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 136cf26c-997a-3819-826b-2eb2a61a18e5 | -14.0313 | -44.5578 | 2025-08-30 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 6df803b6-5f22-394e-b737-5bfd0782e4f6 | -14.4671 | -52.0259 | 2025-08-30 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 5f8549cc-104b-3066-abdb-eb8fa2424e80 | -11.3705 | -43.5868 | 2025-08-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 7425472a-e953-3d77-a8a7-6d605020605d | -9.1337 | -65.8253 | 2025-08-30 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 167.8 |
| 023c13de-16ea-3493-83f0-e2c61d939799 | -9.4498 | -62.3294 | 2025-08-30 13:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 58a36464-8b95-3a6b-ada0-1769b5063156 | -14.0118 | -44.5614 | 2025-08-30 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 173.3 |
| b944592c-847d-338e-bddb-c941ec02ae05 | -6.1853 | -43.3257 | 2025-08-30 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 247.5 |
| 357821d0-9a41-3464-8bd3-5b9418530e8a | -11.3116 | -43.6664 | 2025-08-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 443.8 |
| 0951dbeb-2624-3d4c-b258-e6745026e2a7 | -6.7816 | -43.7632 | 2025-08-30 13:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 834adee3-2333-320a-bb33-feb4dcaf1fa7 | -12.8409 | -48.1907 | 2025-08-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| df4ff54a-88ac-375d-ac31-508f37d9b950 | -13.3623 | -47.018 | 2025-08-30 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 035a7551-d4f1-39b4-a4f4-4b23dd8d68b4 | -12.8601 | -48.188 | 2025-08-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 552a6ab3-34f5-3f47-b9d7-9bb399dad7fb | -6.2096 | -42.7607 | 2025-08-30 13:30:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 108.9 |
| 63b5f294-fcb2-3bb2-b0ac-aa686228ee61 | -9.6758 | -65.0214 | 2025-08-30 13:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 31ef066d-7117-3c3b-8838-a7c4508a1bec | -14.0113 | -44.5849 | 2025-08-30 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 8fb8e1d4-3002-3d74-bdee-1768779c6f16 | -6.1975 | -43.998 | 2025-08-30 13:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| b4d60ab6-6ba1-3bf6-8185-305f08945fbb | -9.7005 | -48.3119 | 2025-08-30 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e33ace45-20e0-3486-be4a-45e1bef952e5 | -6.185 | -43.3491 | 2025-08-30 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 261.4 |
| 4a917436-cdab-35cb-804f-ebdbae437a76 | -9.1338 | -65.8067 | 2025-08-30 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 197e37b0-3354-368f-b2f6-e2e4e667d5ee | -11.3517 | -43.566 | 2025-08-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 245.2 |
| 6d1ec9c7-05b4-3e4e-9c54-df1d8fc0928d | -11.3521 | -43.5423 | 2025-08-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| e38265b8-3354-39e0-ade9-da2e4841c4c7 | -9.1155 | -65.7699 | 2025-08-30 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| cd5e55e6-95bd-363f-bd02-1bf0b03a7a74 | -6.1665 | -43.3273 | 2025-08-30 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 298.2 |
| d78f5ddf-c272-3f3a-9176-eb5c59573f4b | -13.3628 | -46.9953 | 2025-08-30 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 85ee1470-cf9e-3d34-93bf-e0282dbee755 | -11.3709 | -43.5631 | 2025-08-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| a3d4a92f-0c69-32cc-a7d3-178db677fa14 | -13.4986 | -46.9517 | 2025-08-30 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 13ac454a-6754-36bb-8726-f355039f03ce | -8.8665 | -45.7335 | 2025-08-30 13:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 61a1e657-cfbd-3ab8-8894-fa1e06ac38d2 | -11.8952 | -46.398 | 2025-08-30 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 80af4bd6-0b6b-335d-a6d3-6955a0046634 | -9.0799 | -65.4349 | 2025-08-30 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d79d1299-1dad-3289-a2ed-f9692e1edc53 | -12.8413 | -48.1685 | 2025-08-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| fb0872d5-a2e8-315e-84e6-aff92ea37204 | -9.4312 | -62.3303 | 2025-08-30 13:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 1ff7b74e-9a0b-3e92-83ce-33aa13f2a98f | -8.082 | -48.4019 | 2025-08-30 13:30:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| c5dc977d-21d9-3048-bc07-75ac0150dca4 | -13.4793 | -46.9547 | 2025-08-30 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 63.6 |
| f960d03e-ed9e-3476-a2af-e096918721d5 | -13.3632 | -46.9727 | 2025-08-30 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f790ee0f-d7ea-32e2-bb84-917abf1505ce | -11.3125 | -43.6191 | 2025-08-30 13:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.4 |
| b76ed5c9-dcaa-3aa0-8c99-bab7fcfeac55 | -8.8843 | -60.7315 | 2025-08-30 13:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 496de717-a1b5-35a6-8225-dbcb46cac2c8 | -11.7347 | -51.7618 | 2025-08-30 13:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 244.7 |
| d9690fc8-1e49-3400-82d8-569298de7ea3 | -12.6686 | -48.1704 | 2025-08-30 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c897e0e0-fb5e-3e36-8c22-f02c49fbe55b | -7.6033 | -42.6995 | 2025-08-30 13:30:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 88.2 |
| 2fb555b4-801a-3719-b9d7-8053c860df62 | -13.518 | -46.9486 | 2025-08-30 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a7836e07-2e70-36f0-939d-0733527a495d | -6.1975 | -43.998 | 2025-08-30 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| a5854c4d-4464-39f2-8340-f91f18a2c2c6 | -11.3705 | -43.5868 | 2025-08-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| dc2b646a-f4a5-364c-a5e8-b96e964a3079 | -14.105 | -51.7754 | 2025-08-30 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| df495b7a-d766-30f3-808c-dc1bf66172dd | -7.5842 | -42.7251 | 2025-08-30 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| abbfc135-88d7-35c9-a770-c026ef8f41d9 | -9.0799 | -65.4349 | 2025-08-30 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2f2a45de-13cc-330b-99d6-39f14d917165 | -13.3632 | -46.9727 | 2025-08-30 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 97dbfc7e-b834-3b95-b52d-213490aec486 | -13.3623 | -47.018 | 2025-08-30 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 84c7fa89-d8ed-3edd-8ad6-67058dd83860 | -8.3019 | -47.221 | 2025-08-30 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 4e297b6c-d925-3dc3-9fa3-f8d0b7663288 | -11.7347 | -51.7618 | 2025-08-30 13:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 2ee663b4-6419-30bc-abdb-ff85cc52d016 | -9.1337 | -65.8253 | 2025-08-30 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 0cdf8b0c-dd21-3d63-8b77-268a6049fb36 | -6.2284 | -42.7591 | 2025-08-30 13:40:00 | GOES-19 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 21c0e869-7217-31ce-913d-ec2166772b25 | -14.0518 | -44.5071 | 2025-08-30 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 419a34c5-a690-3302-8826-1104276dc572 | -8.082 | -48.4019 | 2025-08-30 13:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c3e12e8b-494a-33bb-936b-87ed5fc64847 | -7.603 | -42.7232 | 2025-08-30 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 125.5 |
| 60b621f0-732b-310c-990d-f3cbfeef92e5 | -11.894 | -46.466 | 2025-08-30 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 03a28a6f-0946-3d7a-b9d2-e5a1a146a525 | -6.1787 | -43.9995 | 2025-08-30 13:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 111.5 |
| b223a519-e4b9-3031-915f-0997b8862076 | -7.0951 | -44.3128 | 2025-08-30 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 044825fa-a35e-32c4-9e7d-48e9ee171526 | -6.1853 | -43.3257 | 2025-08-30 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 9d0bcddb-9e08-3729-a024-ce8c4aa3b7b2 | -13.3817 | -47.015 | 2025-08-30 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 107.5 |
| add93b9e-e169-3bcc-bf32-ffcb98f38315 | -11.8173 | -46.4767 | 2025-08-30 13:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 654c5e94-f6bc-31f6-b5fe-ddbdd30699fd | -11.3125 | -43.6191 | 2025-08-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 47151ba5-e41a-33dd-ba23-b74424f70115 | -9.0614 | -65.4355 | 2025-08-30 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 53319a68-61fc-3a11-a20d-6b9ef4a22b7d | -7.6033 | -42.6995 | 2025-08-30 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 3e57f7fa-8e0f-33b9-b32e-1a1aadcc06fe | -12.6686 | -48.1704 | 2025-08-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 8f7ccd81-8cc9-3312-98db-24d29a9e7a72 | -11.3709 | -43.5631 | 2025-08-30 13:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.9 |
| a534d628-a60c-33e9-b502-b9736eca93b7 | -9.4312 | -62.3303 | 2025-08-30 13:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 5b8c0737-8057-3b8f-8d48-1283b16daf97 | -9.1155 | -65.7699 | 2025-08-30 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| f7119a43-1cba-3883-89d9-afe8acedc6c5 | -13.3628 | -46.9953 | 2025-08-30 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 8bc2a34b-d009-387d-94aa-554e08007d1e | -12.649 | -48.1953 | 2025-08-30 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b1d917e6-b4d5-3bb9-a1ef-ed26f9a5074a | -14.1046 | -51.7967 | 2025-08-30 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |


[Clique aqui para ver as próximas entradas](README101.md)
