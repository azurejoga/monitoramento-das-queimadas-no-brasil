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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c2ba740-bd5c-3903-a9eb-32c2ea12472d | -22.27186 | -55.83488 | 2026-09-11 12:51:00 | TERRA_M-T | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 9eabb733-2662-34c0-aa64-8370babb266e | -9.043 | -65.4175 | 2026-09-11 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a5f814be-6ef5-3bcf-bb8a-cf07c81d3f26 | -9.6951 | -43.3981 | 2026-09-11 13:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 8a7d6614-cf43-35de-82ab-ea3e04bf15c8 | -14.6031 | -48.8379 | 2026-09-11 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.5 |
| c4f22193-5931-340b-9362-6a3ba6360053 | -8.0023 | -43.9931 | 2026-09-11 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 6bf99641-c6e0-3bcb-ac3f-7165c1facdc7 | -14.6026 | -48.8601 | 2026-09-11 13:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| b3812b45-e6f4-3c69-baa6-683014976459 | -7.9831 | -44.0183 | 2026-09-11 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 45d4b6ef-b3f0-3156-b54c-69830c8f9e78 | -7.9645 | -43.9971 | 2026-09-11 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 2e58db13-d619-343a-957c-17e345dc515f | -9.9041 | -45.91 | 2026-09-11 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| d79e0b09-11e9-3d4c-85a1-4bbfa080be89 | -13.268 | -61.597 | 2026-09-11 13:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0c78461d-8ea7-3022-9a09-4ee6f9d6cef2 | -14.0669 | -45.6237 | 2026-09-11 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| c0a5b6f3-c2fe-360d-81cb-a83bdf720273 | -7.9834 | -43.9951 | 2026-09-11 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 066e20f2-6dba-35df-be9e-4dd82b541a52 | -4.8676 | -56.0039 | 2026-09-11 13:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| c3c6a2ef-8040-3fdf-b770-9a955ac9f494 | -13.249 | -61.5983 | 2026-09-11 13:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 3e561088-1e8d-31a2-bdb9-0ac1e17e2b19 | -7.1533 | -45.8766 | 2026-09-11 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 44409d91-607c-350c-9cca-5f83c9789525 | -9.6951 | -43.3981 | 2026-09-11 13:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 7fc79017-a520-34fd-a821-f3c011d556d0 | -10.641 | -46.136 | 2026-09-11 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.7 |
| f777adc9-ff11-3103-b48f-ac6e1a8caf37 | -8.3725 | -47.611 | 2026-09-11 13:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 3ad67bef-ae4e-35f3-b895-ba72f20df5a3 | -7.9645 | -43.9971 | 2026-09-11 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.2 |
| d4dd7815-5304-30fc-8b07-702afa788050 | -13.268 | -61.597 | 2026-09-11 13:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 41a42a5c-ff82-3941-b001-906c801b1482 | -4.8676 | -56.0039 | 2026-09-11 13:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 1c53bd5c-d581-3a7d-8b3f-9af0ac08bae4 | -9.9041 | -45.91 | 2026-09-11 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| c098969c-02ce-3a75-9efa-76e6d8a1675d | -4.3582 | -54.77 | 2026-09-11 13:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 4384930a-2bc0-3a62-b1c0-9a7d806d002e | -8.0023 | -43.9931 | 2026-09-11 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.6 |
| f77382c5-b883-3095-8910-4765c439e289 | -10.5478 | -51.3367 | 2026-09-11 13:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 7442813e-948a-34cd-816e-a190ea7db184 | -9.043 | -65.4175 | 2026-09-11 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 745a7c6c-273b-3e1b-8ab4-a9b5ffb22755 | -14.6026 | -48.8601 | 2026-09-11 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 91.2 |
| a4a9b35b-c23f-31d7-95ce-f36497b52f4a | -7.9834 | -43.9951 | 2026-09-11 13:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e574541d-1fce-39db-b078-de5ebf5686a8 | -14.6031 | -48.8379 | 2026-09-11 13:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| e29b70e7-b50d-30e4-ad11-b99c0fd66630 | -14.0669 | -45.6237 | 2026-09-11 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 6704ae63-834b-398e-a48c-d237d0d8aa0d | -9.9041 | -45.91 | 2026-09-11 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 490.6 |
| 224f4b4e-201e-35cd-b321-697b2a392704 | -7.4595 | -42.1199 | 2026-09-11 13:20:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 102.5 |
| 371aa15b-1dec-31e0-aa4f-c2f6e544dc2d | -7.9833 | -45.5525 | 2026-09-11 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 2e868a3e-d2ad-3034-b9f2-8819041e0e36 | -7.9834 | -43.9951 | 2026-09-11 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 0df826b6-25aa-3c93-b306-53e2d40d08e1 | -14.6031 | -48.8379 | 2026-09-11 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 9153fbd2-b624-35ed-a392-c20c6211cd9f | -8.3725 | -47.611 | 2026-09-11 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| be6b3280-a2fc-3ecf-83af-6b1107867f2c | -10.7959 | -45.9575 | 2026-09-11 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 240.1 |
| cfe5fe60-6a81-37b5-b6a1-026aa8e8c106 | -13.249 | -61.5983 | 2026-09-11 13:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 45525fe4-98ff-35c1-a6d6-aa9b7243c6e6 | -8.0023 | -43.9931 | 2026-09-11 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| dd114fdd-a25c-3801-ac9e-e7e838318d20 | -4.3582 | -54.77 | 2026-09-11 13:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 3c19aefb-0dac-35db-9f65-a5e564638bb0 | -13.268 | -61.597 | 2026-09-11 13:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 108.5 |
| f0b8f085-83a9-3f52-9d2b-1f076bd4c4c9 | -8.0024 | -45.528 | 2026-09-11 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ee3c4605-fbba-3cff-b196-c3cd4e5e9170 | -10.7963 | -45.9348 | 2026-09-11 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 227.2 |
| b0998e0a-80a1-3013-8956-a2097262d808 | -7.9645 | -43.9971 | 2026-09-11 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 572283c6-8b71-3094-9363-4bf5d90791c4 | -9.043 | -65.4175 | 2026-09-11 13:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 8aca9a97-e2eb-3aa4-97de-2929d09dca5e | -7.9831 | -44.0183 | 2026-09-11 13:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 32e5e0eb-8ba9-35d8-a969-001f879df1f5 | -4.8676 | -56.0039 | 2026-09-11 13:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| cc40b3aa-07ee-3ed7-a335-2168ac31433c | -14.6026 | -48.8601 | 2026-09-11 13:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| ef753d6d-5a38-3ef4-aa8e-a7c3cf29d8c9 | -10.5478 | -51.3367 | 2026-09-11 13:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 29203de8-398d-3298-b2f9-57b59f4d6e2a | -8.0021 | -45.5507 | 2026-09-11 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 8ad43297-c6bf-3614-b013-c084e93ad7b6 | -10.5475 | -51.3578 | 2026-09-11 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 209.5 |
| d5fd74cf-af1e-361e-a975-dc6c9eaa3a39 | -14.6031 | -48.8379 | 2026-09-11 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| b95a8f22-2a42-368f-9247-5ba0221967ae | -14.6026 | -48.8601 | 2026-09-11 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 5babaff7-5236-33a7-b67a-785e70feaa5d | -9.9041 | -45.91 | 2026-09-11 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 213.9 |
| feaeed71-ab90-3795-a55e-891db887a535 | -10.5289 | -51.3386 | 2026-09-11 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 5f870910-1e2d-3d75-96f2-deb859d8acc6 | -13.3243 | -61.6709 | 2026-09-11 13:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ef4b49bc-936b-3bde-b141-95af1c0344eb | -10.5478 | -51.3367 | 2026-09-11 13:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 640.3 |
| 1fba072b-e555-37c4-afe2-5a0e3b3426ab | -4.3582 | -54.77 | 2026-09-11 13:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 9ea90fea-247a-364b-9a51-66a7f90c6366 | -9.6951 | -43.3981 | 2026-09-11 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 89.9 |
| 662e0515-c369-3513-b87d-0afe345fc0db | -14.0669 | -45.6237 | 2026-09-11 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 278285fc-c1bf-371e-8a20-22cc07585e1e | -10.641 | -46.136 | 2026-09-11 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| d8f436d7-27b4-3c3d-9054-5884723d0783 | -9.043 | -65.4175 | 2026-09-11 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| c19d3c94-f976-3fc7-934c-e0451a6266e4 | -9.0244 | -65.4181 | 2026-09-11 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| fe73be6a-b41b-3d0c-b1d6-fa0439c64c79 | -10.2182 | -45.2111 | 2026-09-11 13:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| aef9f67a-633e-3c44-84f5-805d87feb120 | -4.8676 | -56.0039 | 2026-09-11 13:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| ff420a42-e84e-3385-9f87-5c2e492c0aa5 | -7.9645 | -43.9971 | 2026-09-11 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 116.4 |
| c106a573-40ac-3d7b-a07c-925b7f34a678 | -7.5553 | -45.1624 | 2026-09-11 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.7 |
| f405067e-b84b-383d-8425-916ec4fb5c3f | -9.0431 | -65.3988 | 2026-09-11 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 3379593f-e614-3fc5-83ef-beb5b4e45b6f | -13.268 | -61.597 | 2026-09-11 13:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 745d0a09-daf3-3838-a84f-d40cb7db98b4 | -13.3433 | -61.6696 | 2026-09-11 13:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 298003c7-a164-34f1-aea6-a494fa4b4f63 | -7.9834 | -43.9951 | 2026-09-11 13:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| a5bf2b31-abeb-3218-80dc-541fd63eaa00 | -9.9041 | -45.91 | 2026-09-11 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 398.3 |
| 54b299fd-764e-3039-91ab-0de979cbfe57 | -11.0434 | -49.6851 | 2026-09-11 13:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| b9a0df2c-e21e-34ed-a14b-8ec2eb9e94cb | -22.2649 | -55.8315 | 2026-09-11 13:40:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 218.4 |
| 545ce467-15ed-3b60-a56f-0feaa5f240ad | -14.5836 | -48.8409 | 2026-09-11 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 5936fda0-0af5-3c3a-bfbc-0ba768ae7a77 | -7.9831 | -44.0183 | 2026-09-11 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4c5bf798-d920-360e-8b70-da95587f2a8d | -9.0431 | -65.3988 | 2026-09-11 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 0908fdc6-5c7c-3d25-86f6-893ad0c457e8 | -7.9645 | -43.9971 | 2026-09-11 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| a0121638-5f3e-3b0e-9b2d-861aff763fd8 | -7.5193 | -45.0293 | 2026-09-11 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 860fb015-5938-3a25-9a18-52b4cb871841 | -10.5478 | -51.3367 | 2026-09-11 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 245.8 |
| f2c24de4-992f-379a-8c8f-ec410edcce64 | -10.7959 | -45.9575 | 2026-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| a289b1db-5219-3551-9085-105163a6c318 | -11.3513 | -45.7922 | 2026-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 205.4 |
| f305841e-4ec7-3f82-8fcb-a548d001c2ee | -6.7267 | -45.4394 | 2026-09-11 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d69ef837-23be-3246-b16a-270ed97162df | -9.043 | -65.4175 | 2026-09-11 13:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 295f14eb-116e-3d6c-b898-a04658ad7a7f | -13.2297 | -61.6384 | 2026-09-11 13:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 89b7cb60-21df-3f7f-afee-230710e34ffa | -14.6026 | -48.8601 | 2026-09-11 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 151.9 |
| 390b32c1-4665-3f1e-a0e2-4ecd60bccf7d | -13.3243 | -61.6709 | 2026-09-11 13:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e92ec269-99e0-3e11-80e4-866d1100a472 | -13.249 | -61.5983 | 2026-09-11 13:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3a5cbf29-1a55-3f4d-9355-786ebd056074 | -13.3433 | -61.6696 | 2026-09-11 13:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| f5dcaf1d-55d3-3d0c-a8e6-2829352b8b25 | -22.2645 | -55.8532 | 2026-09-11 13:40:00 | GOES-19 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 32abb327-9d66-34a2-8104-211009414090 | -10.7963 | -45.9348 | 2026-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| f2973f11-0b49-3df9-93a6-4c3cc9f4b62f | -13.268 | -61.597 | 2026-09-11 13:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 51e9af1c-4100-35ca-8e7d-e55f3e1076f1 | -7.9834 | -43.9951 | 2026-09-11 13:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 37d4a19d-9769-3a7b-95f8-5a9750093342 | -10.7359 | -46.1465 | 2026-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| e01ab46a-58d3-3fc2-9be4-281eddb9e033 | -4.8676 | -56.0039 | 2026-09-11 13:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b04e987d-aa48-3c10-8ebb-21d19b0a996b | -14.6031 | -48.8379 | 2026-09-11 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 197.1 |
| f4c99e33-7c26-3e11-b788-24dfb1bf1869 | -4.3582 | -54.77 | 2026-09-11 13:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 184.4 |
| a8d50330-73f3-3344-8a2f-5102ac43c519 | -10.7674 | -60.7666 | 2026-09-11 13:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| c7c1e477-a91d-3457-81b2-4696d0dd38ba | -10.5475 | -51.3578 | 2026-09-11 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 137.8 |
| 5e334435-5d8b-3125-8a78-b321f0875e09 | -11.3326 | -45.772 | 2026-09-11 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |


[Clique aqui para ver as próximas entradas](README39.md)
