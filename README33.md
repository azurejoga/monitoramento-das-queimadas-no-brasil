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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25297baa-6b18-3670-a935-98bd6c09d51b | -12.0803 | -50.2535 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| f9738aac-6ef3-3990-a442-a64446ee717a | -12.0155 | -50.7541 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 5a8df3ce-89cf-31a9-adb6-77d398e9a557 | -11.6567 | -50.5817 | 2026-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 64bdf37b-046f-381e-a51e-a1e6e0114f3a | -11.9392 | -50.7629 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 07262971-b95b-3b0a-9c29-9157e13b31bd | -6.2587 | -41.6377 | 2026-09-26 13:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.7 |
| a5060a43-0ea1-3348-87e6-a4d36e221ad2 | -13.8151 | -51.8553 | 2026-09-26 13:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 28c0b892-a746-3fbf-bd76-4ff766b2df3a | -11.9405 | -50.6773 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e5bf4ca1-30c6-3c09-91ea-3527cbc9c6ee | -11.9402 | -50.6987 | 2026-09-26 13:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 92.8 |
| d9fe30a3-068e-3fa8-b3bf-ae660cf49c93 | -13.8151 | -51.8553 | 2026-09-26 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| fb930bb6-2c97-3471-82fa-b880a83c73cc | -14.2219 | -48.5198 | 2026-09-26 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 739e49e6-d0da-3b7c-8179-2dcfca227fc8 | -15.4322 | -41.5199 | 2026-09-26 13:30:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.6 |
| 0031ff60-6ac1-312c-8c57-97557a05466e | -17.5639 | -46.3458 | 2026-09-26 13:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 92506783-2a23-302f-8e28-86b5bd588066 | -12.2636 | -50.7248 | 2026-09-26 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 6d4a7568-64d5-3c81-9a91-eb977fab1a0a | -17.5445 | -46.3266 | 2026-09-26 13:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6dffb92d-3a17-366a-8541-fcb6b71755de | -12.2827 | -50.7226 | 2026-09-26 13:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 049ab17a-f072-38bc-93c5-58ede85e39b8 | -12.1557 | -50.3089 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.2 |
| fef85449-9d44-30cc-a0d5-1e7902aa15ae | -13.8343 | -51.8529 | 2026-09-26 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 5966fa34-2e41-3a98-a510-9c278e3d71aa | -11.6199 | -50.5004 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 94f418b3-658f-3ce7-99c2-5c0b6d8fb046 | -11.6009 | -50.5025 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 4a17fa8d-cbf1-3d3b-bc2c-a2342ac14f17 | -7.0071 | -42.0943 | 2026-09-26 13:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 4c7e7d18-f8fe-39e8-b13e-8979628caabf | -12.6844 | -47.2767 | 2026-09-26 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 8f3ba11e-afe4-3d12-8f56-9dfdf98fd2f5 | -12.2508 | -50.3189 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| f26c99fd-7c9a-3e25-a600-5c33c01e722e | -12.1553 | -50.3305 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 142445ea-661f-37f6-82e7-7f14b4994d60 | -12.0365 | -50.6233 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| e85a5e6b-3094-3046-8122-01b883ae8f6a | -7.3656 | -42.0819 | 2026-09-26 13:30:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 190.9 |
| 669a9a2b-3805-39e8-84ce-bb588d85eaa1 | -12.1366 | -50.3112 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 8f3aee30-b4c8-3f4b-aef2-1923719845d2 | -12.2696 | -50.3381 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.7 |
| af20985e-5f41-34fb-afea-348da7e755b8 | -13.8579 | -46.3713 | 2026-09-26 13:30:00 | GOES-19 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 940758a9-4d41-3930-a761-eba6b09f3bda | -6.2401 | -41.6153 | 2026-09-26 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 59f3853c-f6dc-3514-a7ab-107adc751409 | -11.7107 | -50.7891 | 2026-09-26 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 3728e8f8-60dd-3162-a12a-46cc80563ed9 | -14.2223 | -48.4975 | 2026-09-26 13:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 87ef2816-944b-38b6-b6ce-9fdf436c07f0 | -12.2699 | -50.3166 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| f828073e-04e0-3b73-b7a6-03eb7d1cd468 | -12.9457 | -51.0695 | 2026-09-26 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| b25f27dd-2850-3dab-91ae-7a605fba8027 | -12.2123 | -50.3451 | 2026-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 4239539f-e0fa-30a3-baef-57d22e7dc5e4 | -12.6651 | -47.2795 | 2026-09-26 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.8 |
| b69414da-1d19-35ab-b41e-b2685f30843f | -6.2587 | -41.6377 | 2026-09-26 13:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| 5a473328-ffec-3c95-94c1-4262200f779e | -12.723 | -50.6475 | 2026-09-26 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 93344602-556b-3d12-b046-97558be878aa | -11.7107 | -50.7891 | 2026-09-26 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 3fafc44b-c3fe-38c9-9491-ef1a0a44bc54 | -12.1366 | -50.3112 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 6e486f34-188c-3702-9774-b285ac3c3436 | -14.6898 | -45.5831 | 2026-09-26 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 9dd2b725-719f-38e3-a288-b0c21aa58eaf | -12.9457 | -51.0695 | 2026-09-26 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 1c020c72-4341-3d1b-a888-534da2f986cc | -11.7297 | -50.7869 | 2026-09-26 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 7f0fbf9a-a810-3237-b0a5-78af3a192e44 | -11.9228 | -50.5938 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e89a2a66-e396-3afb-8999-8cd32bbbd4af | -14.2223 | -48.4975 | 2026-09-26 13:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 19a69b39-3c04-30aa-8f06-f4833381186b | -12.1553 | -50.3305 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 107a4e25-51ce-322e-80de-60e47b1f4a13 | -13.8154 | -51.834 | 2026-09-26 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b22fbb50-6718-3e2f-8070-3ee4e2168930 | -6.2401 | -41.6153 | 2026-09-26 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 107.8 |
| 21c2e8e5-1f0c-3c7f-b99e-de92b018a33b | -15.4322 | -41.5199 | 2026-09-26 13:40:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 137.4 |
| ca63a0a0-a06e-396c-b56f-79a429d4d629 | -12.0556 | -50.6211 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 98fa5b1b-e077-3e12-9364-5a01deacdb35 | -14.6893 | -45.6064 | 2026-09-26 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 2a50ef0f-6a09-3a88-aeef-dc96e9bc2301 | -13.8151 | -51.8553 | 2026-09-26 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 6d52eaf9-c233-3f75-878d-643ed921d02d | -11.9418 | -50.5916 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| dd5a01d1-cb8c-3798-8e34-5a51c4011869 | -13.8343 | -51.8529 | 2026-09-26 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 044ef930-8467-32aa-9824-cec3ee6b861a | -11.8665 | -50.5362 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 7a10f69a-fa41-3ba8-9a94-105005952fb9 | -12.3478 | -50.221 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 20703676-5648-37de-bc08-dfe19d172e1b | -13.7958 | -51.8578 | 2026-09-26 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| badbcd2d-342a-361d-934f-6dc69881cfd2 | -7.1392 | -42.0811 | 2026-09-26 13:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| ec9439fe-b918-351a-b79f-85bba3b578e6 | -13.5542 | -40.6497 | 2026-09-26 13:40:00 | GOES-19 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 739d0f2c-f28e-3517-8f5a-cc3f21313ce7 | -7.2758 | -43.2975 | 2026-09-26 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 1cfd93da-6a0e-3eaa-9754-7016cdaf2080 | -12.1557 | -50.3089 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 5ed8fcec-04e8-35ac-8a1c-aa24e3bb9b6a | -12.0365 | -50.6233 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 97a17175-1ed5-3230-9fb3-e9c4ecb4857d | -6.2587 | -41.6377 | 2026-09-26 13:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 115.8 |
| b82ded85-9a75-32c5-a2a6-05d408df17a1 | -12.1369 | -50.2897 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 0487b6dc-72d1-3885-a39a-4fac6a1781c9 | -7.2569 | -43.2994 | 2026-09-26 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| b3871895-23f3-39ea-b03b-e1ac01a648d1 | -12.2123 | -50.3451 | 2026-09-26 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| e4330afc-4c25-3ba7-839b-35aff6d11e38 | -8.7927 | -45.6056 | 2026-09-26 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 14b40ff3-9b53-3ab9-906d-00bb3184e3af | -13.5484 | -52.9227 | 2026-09-26 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| bc811777-ee37-342e-a573-05687125e450 | -15.4322 | -41.5199 | 2026-09-26 13:50:00 | GOES-19 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 166.6 |
| e3b484b7-9c1e-3996-81ca-a31e9aef394a | -6.2401 | -41.6153 | 2026-09-26 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 112.4 |
| 853bd0bb-5800-3208-9629-3d818d3a99dd | -11.7107 | -50.7891 | 2026-09-26 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 1e3b3289-6db4-30df-9c57-099c0d08847b | -12.4977 | -46.9892 | 2026-09-26 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 8c91a0a9-35bc-3129-8fa3-d9115b4cbeb1 | -13.5542 | -40.6497 | 2026-09-26 13:50:00 | GOES-19 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 197.0 |
| 26c29c78-8dc9-3f51-b734-5506fb0bf91d | -13.7142 | -48.8172 | 2026-09-26 13:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 18c824b2-1d3f-33ef-b190-47f37c2793e1 | -13.7146 | -48.7951 | 2026-09-26 13:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| d7dc2438-71bd-390d-9bfa-9ca3a7bdf13c | -12.723 | -50.6475 | 2026-09-26 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 1199f095-41b6-3844-9023-11791550fdbd | -13.8343 | -51.8529 | 2026-09-26 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ec65d10e-5490-3a4e-8c20-5adf4affc160 | -11.0233 | -54.0559 | 2026-09-26 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 29473749-8617-3ff4-9488-3e24027334ac | -11.8014 | -49.8129 | 2026-09-26 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.0 |
| b5ffd1d6-aef6-38ad-8ab7-185752b75aab | -12.4973 | -47.0118 | 2026-09-26 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| ed2e35a6-7569-3d08-b15b-57cdc192aaa6 | -12.0556 | -50.6211 | 2026-09-26 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 5d2beab9-c43d-3d0f-8193-04abebcfe71a | -6.8408 | -43.5021 | 2026-09-26 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 740.7 |
| 42f58b34-037c-321a-b254-912a2238ad6b | -10.872 | -54.0899 | 2026-09-26 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 221c1c3c-c4cc-3a92-9bb6-238fd943dec4 | -3.8604 | -44.0585 | 2026-09-26 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b776ee73-5cf2-3b86-ad3e-a104fdc66246 | -13.7958 | -51.8578 | 2026-09-26 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 745f7085-d8e4-3211-9cb3-e2d2d2309a6f | -17.5445 | -46.3266 | 2026-09-26 13:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 20fec7b8-e4c6-377d-8521-28c649be8a3f | -14.2223 | -48.4975 | 2026-09-26 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 87fed64a-bfd8-3de8-b909-8546bd496cac | -12.4784 | -46.992 | 2026-09-26 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 5d191ae3-0ee0-3a3d-ba9d-033fd2b8c4c3 | -14.6898 | -45.5831 | 2026-09-26 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 8c3ffc41-fd4b-3416-9669-77cba74c6a39 | -14.2299 | -49.1157 | 2026-09-26 13:50:00 | GOES-19 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| f387effc-d3dc-318e-bd19-738a749e5b63 | -13.8151 | -51.8553 | 2026-09-26 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 9bf810bc-22ec-3bc7-9444-60c685869e94 | -7.0071 | -42.0943 | 2026-09-26 13:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.3 |
| 4065eff0-0926-386e-889a-d1144f8b7d51 | -12.44 | -46.9975 | 2026-09-26 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| d0a5623b-8aa5-3087-a0f6-757a760ecc19 | -13.5487 | -52.9016 | 2026-09-26 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 112.2 |
| ec29d115-c914-3b82-9096-62d3ca4fe6ad | -6.2587 | -41.6377 | 2026-09-26 13:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 116.4 |
| d86cfcfa-844a-3af4-b543-34e4a6d33913 | -10.9358 | -50.5972 | 2026-09-26 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| d558c883-e974-397d-b8af-2e82da0c630d | -13.8154 | -51.834 | 2026-09-26 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 7b22391f-eaa7-3593-bfe9-3f285d0a1161 | -11.7297 | -50.7869 | 2026-09-26 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 4f017672-2eb8-3ec8-82d5-0d78e3d99002 | -14.7671 | -45.6155 | 2026-09-26 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 385bc13a-e23d-3b8e-a0a4-c123ee777315 | -13.5295 | -52.9039 | 2026-09-26 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| a313ecfb-408f-3f16-8d0e-61cf59f04629 | -11.118 | -54.0268 | 2026-09-26 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |


[Clique aqui para ver as próximas entradas](README34.md)
