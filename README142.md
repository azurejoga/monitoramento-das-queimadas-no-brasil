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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4c0d756-bfe5-3cf4-96a3-1b76b9210f8b | -9.49611 | -63.13516 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 962da89b-7712-3c7a-9fa5-73d3a181e6bd | -7.86945 | -71.71526 | 2025-10-02 06:12:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c7686d29-9290-3c84-9e61-6b699deb911b | -9.40503 | -63.69744 | 2025-10-02 06:12:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a58fb84-69fc-3e3c-a723-58e99fa1387b | -9.64657 | -62.84671 | 2025-10-02 06:12:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 52d8794a-4ada-368b-961a-0d851a827f2e | -9.64704 | -62.8432 | 2025-10-02 06:12:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4cf5f15-ac1a-3731-a0e0-bd0eee2084b3 | -9.72245 | -64.20523 | 2025-10-02 06:12:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68c6ed56-51dc-309e-8dfe-9ab8784467de | -16.0025 | -50.902 | 2025-10-02 07:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 4e1e6ba2-c5cd-388a-9278-c074e0299560 | -19.6956 | -47.6261 | 2025-10-02 07:00:00 | GOES-19 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| ff0365d8-9c12-300a-8c88-eb33c4b90702 | -16.0421 | -50.874 | 2025-10-02 07:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 35.3 |
| ad45b111-a5c4-34c1-99e0-31a62ca7396b | -16.0025 | -50.902 | 2025-10-02 07:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 76ab6344-18de-38ac-bf11-7bce101b2363 | -16.0421 | -50.874 | 2025-10-02 07:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 9363bbd6-9f94-34c1-a9ab-3d7f3aece7cf | -17.1897 | -47.025 | 2025-10-02 07:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 647997dd-95ec-30a7-86e5-eed917a0ecfe | -16.0221 | -50.8989 | 2025-10-02 07:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 0216874a-63cc-30d6-ada0-b8d9f6e97a05 | -16.0025 | -50.902 | 2025-10-02 07:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 32108028-3e30-3291-890e-04a89981e454 | -16.0421 | -50.874 | 2025-10-02 07:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| a7f60b75-5dea-380e-979a-e99180576275 | -13.7962 | -47.5362 | 2025-10-02 07:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 27bc9b1c-46f3-35a5-82c2-c15a49f22a10 | -16.0421 | -50.874 | 2025-10-02 07:50:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 38.1 |
| fafbb287-0ecc-3f85-a89c-f299f6679000 | -13.1542 | -47.8568 | 2025-10-02 07:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 690fee6a-53b8-30dc-8c06-3160d9b87335 | -13.1542 | -47.8568 | 2025-10-02 08:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| c03e5781-486d-3a03-9e06-51510f9eed1a | -14.4255 | -46.115 | 2025-10-02 08:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1135780a-57d2-339a-8a6d-3c855afead27 | -16.0421 | -50.874 | 2025-10-02 08:00:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 05d6ba1f-cd05-351e-8608-44fd08e58f13 | -13.1542 | -47.8568 | 2025-10-02 08:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| b99d8962-0d77-3786-bae6-2ba684b0ac74 | -16.0025 | -50.902 | 2025-10-02 08:10:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 4d998cba-d3b2-3911-a5a1-53297a11a491 | -13.1349 | -47.8597 | 2025-10-02 08:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8059d034-b76f-3762-af1c-35562c388fd9 | -14.4255 | -46.115 | 2025-10-02 08:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ea665abf-9b77-3bf5-a59d-182b7b077aaa | -16.0421 | -50.874 | 2025-10-02 08:10:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 027bfa35-4582-3aa0-8da0-ed487c4c1769 | -16.0025 | -50.902 | 2025-10-02 08:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 98f9f75c-24ad-34ec-9ac0-2bd877e326f2 | -16.0421 | -50.874 | 2025-10-02 08:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 0b7101a1-997c-3a12-ac40-f1f0cebe5fa2 | -11.0331 | -46.6045 | 2025-10-02 09:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 300.8 |
| d5923591-efd6-3d16-9057-44df411ab851 | -11.0521 | -46.602 | 2025-10-02 09:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 326.9 |
| 6019b7b5-2bd1-3ed9-a275-ef65f44e2a7d | -11.0518 | -46.6246 | 2025-10-02 09:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 381.4 |
| 010a2163-1cbc-36d8-b8b4-d6dc9e600e3b | -11.0327 | -46.627 | 2025-10-02 09:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 370.9 |
| 63fdc25b-a0eb-3423-acdb-36512c346487 | -11.0327 | -46.627 | 2025-10-02 09:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 344.1 |
| c0d0aeed-6c8a-3a20-8882-70821b644255 | -11.0518 | -46.6246 | 2025-10-02 09:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 359.5 |
| c72c39af-6afe-3aa1-95f2-d25759fcf814 | -11.0521 | -46.602 | 2025-10-02 09:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 316.5 |
| b6201c6c-fae0-340c-a788-b43e2984af05 | -11.0331 | -46.6045 | 2025-10-02 09:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 338.5 |
| 24aa6e22-9c34-317c-ae8a-8ef9d9f71df9 | -11.0327 | -46.627 | 2025-10-02 09:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 214.8 |
| b09e3749-53d0-3fb2-8b40-c9ebf51ce325 | -11.0331 | -46.6045 | 2025-10-02 09:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 489.1 |
| bd9be49f-2cb8-34d7-85b7-c3d0d6acddc3 | -11.0518 | -46.6246 | 2025-10-02 09:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 304.2 |
| be6d1068-f057-3f90-8cdc-67d7fa6db61d | -11.0334 | -46.582 | 2025-10-02 09:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 1949828e-dd42-3b77-9be0-a9a1b8dad8f2 | -11.0521 | -46.602 | 2025-10-02 09:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 476.5 |
| 3bf1dce7-7ae1-348e-8453-4430032c2d36 | -11.0331 | -46.6045 | 2025-10-02 09:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| b1e4666d-6782-38ea-a25d-beeded973321 | -11.0518 | -46.6246 | 2025-10-02 09:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 405.2 |
| 5e844153-272a-3b1d-abb0-5a5876d4cf9d | -11.0521 | -46.602 | 2025-10-02 09:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 358.7 |
| d1444c7b-b113-34fd-967e-02a36e2b7d38 | -11.0518 | -46.6246 | 2025-10-02 09:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 150.7 |
| ab317eb5-2e92-3ceb-a2ec-4fcfa3c14e28 | -11.0521 | -46.602 | 2025-10-02 09:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 233.7 |
| d8a7379a-0ffb-34ad-8ba7-ba5b649df0ea | -11.0521 | -46.602 | 2025-10-02 10:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 278.2 |
| 8545ba8e-6933-31d3-82bc-d68913cf2825 | -11.0518 | -46.6246 | 2025-10-02 10:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 11839367-0b62-3263-a302-68c26dc9cf99 | -11.0518 | -46.6246 | 2025-10-02 10:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 492.0 |
| 6976b06e-fe93-39b4-923b-6997e73615c9 | -11.0709 | -46.6221 | 2025-10-02 10:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| b92b1f7c-d38e-3de3-90b8-9a4ba96cb844 | -12.2773 | -45.3834 | 2025-10-02 10:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c225ea78-1aec-3972-be64-4f9d8ac8c452 | -11.0521 | -46.602 | 2025-10-02 10:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 207.6 |
| d6706569-dba9-38a9-b460-7f5168f45161 | -11.9276 | -47.8719 | 2025-10-02 10:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| cf3827de-e10c-31a3-9055-ca03bd116ba7 | -11.9085 | -47.8745 | 2025-10-02 10:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 719789c5-a391-3f53-8786-c0e1a4628156 | -9.9178 | -43.7447 | 2025-10-02 10:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 108.2 |
| d6cca559-b012-31e2-9648-f0baf10797e3 | -14.1921 | -46.1321 | 2025-10-02 10:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 4406faf9-7322-371d-8e42-f40ad59e6c87 | -13.1542 | -47.8568 | 2025-10-02 10:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| c86b0c3e-9ec6-3f01-a135-8ca76a04fe81 | -11.0518 | -46.6246 | 2025-10-02 10:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 0da883f5-ba88-3b27-923c-9d37a32b9c2d | -12.2773 | -45.3834 | 2025-10-02 10:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 265.8 |
| 5b9c697f-56ab-3c3d-b698-257c5c9b03ec | -13.1349 | -47.8597 | 2025-10-02 10:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 2c019e10-529d-37aa-b492-52d393bd98ae | -12.2777 | -45.3603 | 2025-10-02 10:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| fe7e66a8-d04f-3a0c-b0cf-f58df12eaa3d | -11.0518 | -46.6246 | 2025-10-02 10:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 134.8 |
| a8db6809-638d-3d08-9b09-3037c4704cbc | -9.9369 | -43.7422 | 2025-10-02 10:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 1f47990b-76e3-3766-97e0-afd65fe8cfc7 | -13.1542 | -47.8568 | 2025-10-02 10:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| ebfde895-f10f-3370-ba8f-3c42dfbe7c5b | -11.9276 | -47.8719 | 2025-10-02 10:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 148.8 |
| e2254c71-670f-3c0e-81df-d7d4cf275f67 | -11.9085 | -47.8745 | 2025-10-02 10:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 170.6 |
| 5eb21d65-0252-3d32-b987-f99c3e80a709 | -14.4757 | -48.4137 | 2025-10-02 10:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 82c36c88-bf50-3ac4-946e-fbb28f26374c | -19.4144 | -46.8271 | 2025-10-02 10:30:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 54727106-4dc2-3870-a6d6-0d6522b6a1c4 | -13.1349 | -47.8597 | 2025-10-02 10:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 52a73e7a-84d3-365c-bb8e-b4b6059b3978 | -11.0709 | -46.6221 | 2025-10-02 10:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| fc69e761-7b97-39f6-8b54-90f9b2b0fbf6 | -12.4182 | -45.0385 | 2025-10-02 10:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.0 |
| e0e938c0-4d2f-38c9-9206-25ff632c31cb | -11.0327 | -46.627 | 2025-10-02 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 0557186e-a166-3301-bf74-75dd87cfff48 | -9.9369 | -43.7422 | 2025-10-02 10:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 137.7 |
| 8007a692-9c4c-33c2-9ac4-a579c7c0c7d9 | -11.9276 | -47.8719 | 2025-10-02 10:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 219.2 |
| 7c98c441-e766-3de2-913e-adf283ff0ef0 | -9.9178 | -43.7447 | 2025-10-02 10:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 3961153e-f1c4-39d7-8446-28d9d75934b2 | -11.9081 | -47.8967 | 2025-10-02 10:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 164.1 |
| d39f643d-c842-30fc-ace1-50e76e8d5e96 | -12.4182 | -45.0385 | 2025-10-02 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 44e411b1-4fab-3676-abb7-77afc81fa7ec | -14.4757 | -48.4137 | 2025-10-02 10:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 1f96e136-43d9-39db-a902-dceb02e76966 | -12.4186 | -45.0153 | 2025-10-02 10:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| eb49714b-c7c9-3ad3-8163-a65cfef03f77 | -11.9272 | -47.8941 | 2025-10-02 10:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| a398fe30-5948-3939-b5f7-ee1e8c8d5541 | -11.9088 | -47.8522 | 2025-10-02 10:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ef96580d-5dc2-337e-81e4-c0e24f79a5ac | -9.9372 | -43.7187 | 2025-10-02 10:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| f6fa5dc5-4616-3082-bf59-2e6a2810486d | -11.0324 | -46.6496 | 2025-10-02 10:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| c9ae1298-8ad6-3b87-a9f7-0242211306d1 | -11.1746 | -47.2805 | 2025-10-02 10:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 04d073e8-b793-327b-8a39-8cb79219c003 | -13.1349 | -47.8597 | 2025-10-02 10:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 0ab92edb-5784-393c-9a16-f7b798ebb26e | -11.9085 | -47.8745 | 2025-10-02 10:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 517.0 |
| 38fca2dd-a1e4-3282-a698-d7c1e59698b2 | -11.9276 | -47.8719 | 2025-10-02 10:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| acb56672-8cd2-3480-a348-3bd372de13cd | -13.1349 | -47.8597 | 2025-10-02 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 054d6fd2-efd0-39d8-923b-83337e82048d | -14.4255 | -46.115 | 2025-10-02 10:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 08431cdd-c499-391d-b8bc-e42b1a78e07b | -11.1937 | -47.278 | 2025-10-02 10:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| acbed44a-e262-394f-b853-ea311c5b5beb | -14.1921 | -46.1321 | 2025-10-02 10:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| b3d6192e-7c2f-3f51-a278-c2629e810035 | -9.9178 | -43.7447 | 2025-10-02 10:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 101.2 |
| f33e6727-d2cf-3267-8ee0-cbf2167505aa | -11.9085 | -47.8745 | 2025-10-02 10:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 205.1 |
| 2a9027b6-86db-310c-9f54-46da827b97cf | -11.9081 | -47.8967 | 2025-10-02 10:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 0658b9bd-0ac2-3901-bea1-99d6cb647887 | -12.4182 | -45.0385 | 2025-10-02 10:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| ac285ed6-2e30-3542-9127-8a15c4d9da92 | -11.0324 | -46.6496 | 2025-10-02 10:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 158fe878-1bd5-3327-abe0-752054a51a28 | -14.425 | -46.1381 | 2025-10-02 10:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 452ee152-5e13-3899-a346-8b1ede6bf03b | -13.1542 | -47.8568 | 2025-10-02 10:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 07bdb031-58a1-3be9-97a4-eb40ec56b247 | -11.0327 | -46.627 | 2025-10-02 10:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 7e77ceff-b175-3151-9a6c-cbcef484107b | -14.425 | -46.1381 | 2025-10-02 11:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |


[Clique aqui para ver as próximas entradas](README143.md)
