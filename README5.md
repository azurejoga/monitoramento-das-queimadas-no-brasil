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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 744299ed-8cd7-36e0-95ad-22026abc237b | -5.78 | -57.5605 | 2026-08-24 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| bd5d47f2-2c7e-3a9f-915d-b32f33f5a86b | -12.075 | -50.5974 | 2026-08-24 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1ebf2355-32f5-3f57-8b3b-76588cf197ab | -12.0753 | -50.5759 | 2026-08-24 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| ef4528f4-8f78-3e61-a954-f5f3206b3c57 | -12.1224 | -43.3977 | 2026-08-24 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| c9bd2a3e-85b1-3955-a633-9822c62038da | -6.5487 | -58.522 | 2026-08-24 00:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| d3554994-1817-3d70-9198-b23de8608241 | -7.3788 | -45.8344 | 2026-08-24 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 156.4 |
| f2dd1f71-bea1-3fdb-b526-128f1e4f192c | -6.6048 | -58.3838 | 2026-08-24 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 37ec5c29-20b9-38da-b27d-fe71bfc82359 | -6.7451 | -59.6533 | 2026-08-24 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 04549689-a692-3f97-ac89-99abbaaf35e9 | -12.0938 | -50.6166 | 2026-08-24 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 69a673e2-c3f0-3d7f-ad97-8191a05aca1c | -8.9876 | -65.3819 | 2026-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| a3925e86-13eb-382d-bbc7-81813c9ac693 | -6.8008 | -59.5934 | 2026-08-24 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 9cea9fb9-86e4-31e8-bb21-3da659356005 | -8.9875 | -65.4006 | 2026-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e651ef9b-4ad5-38df-a74b-ca229c723763 | -22.9932 | -49.3831 | 2026-08-24 00:30:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| bfcfe6d9-592b-3105-a129-46cb93e567b8 | -9.006 | -65.4 | 2026-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 718d6742-6a38-336a-9e5b-b50adb40d850 | -3.5406 | -48.1889 | 2026-08-24 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b7d45765-e22a-3fa9-95e8-3e23af289198 | -6.3505 | -54.7665 | 2026-08-24 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 848d8f78-d75e-39be-87cd-9c2737a99067 | -7.3791 | -45.8119 | 2026-08-24 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 249.9 |
| 7d4480fd-67c3-3658-a222-212192cf80bb | -6.6233 | -58.383 | 2026-08-24 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 44227d10-fa6d-3c82-9772-40afd74e5f51 | -7.3603 | -45.8136 | 2026-08-24 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 286.0 |
| 7928da60-9693-3c22-8975-a0126e57aaa8 | -9.0061 | -65.3813 | 2026-08-24 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| a0b694ad-029e-3b2d-bedc-8b1aa4499924 | -7.3605 | -45.791 | 2026-08-24 00:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 169.7 |
| c0cdb764-42ab-3f49-89a4-c2529a8cf23b | -12.0944 | -50.5737 | 2026-08-24 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 564d67f8-2ae1-356d-b00c-f0753871769d | -23.0142 | -49.3779 | 2026-08-24 00:30:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.1 |
| 99e28e70-f609-3cbd-9d3c-02d514815388 | -12.1417 | -43.3945 | 2026-08-24 00:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 111.1 |
| f5e953a4-0126-3157-98fe-34afa29468e7 | -6.6048 | -58.3838 | 2026-08-24 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 50bc26a5-d1b1-3949-ba67-dc10302c6e4e | -7.3605 | -45.791 | 2026-08-24 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 159.2 |
| ea69e9a9-0b90-336c-be67-1bf432432070 | -17.444 | -48.8199 | 2026-08-24 00:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d6dda6e0-540b-3a93-b8cd-fdfd63133915 | -9.0061 | -65.3813 | 2026-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.8 |
| 3a47672c-26bd-391b-9e6c-36189b23f6e4 | -7.3793 | -45.7894 | 2026-08-24 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 25216384-db2d-3987-a85e-365d3a6833e2 | -17.4241 | -48.8236 | 2026-08-24 00:40:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| ea633883-fa37-37f4-86b8-f2d6fe327717 | -11.9269 | -55.9077 | 2026-08-24 00:40:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1d0b95d0-6ce4-3a46-8773-befd854e732f | -8.9876 | -65.3819 | 2026-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| bbc998be-12ab-350e-aade-ebd665bd6ffe | -23.0149 | -49.3545 | 2026-08-24 00:40:00 | GOES-19 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.4 |
| b9651dad-b8e1-3017-a331-d45ee380fc65 | -11.9079 | -55.9093 | 2026-08-24 00:40:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| e2f062e1-b382-3e64-b376-9942d299c1c6 | -7.3603 | -45.8136 | 2026-08-24 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 382.7 |
| 62c5adfe-0d58-3230-9472-e5f10e4bef6e | -12.0944 | -50.5737 | 2026-08-24 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e625468a-e12a-389b-8c20-073efcc9e8d5 | -22.9932 | -49.3831 | 2026-08-24 00:40:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.3 |
| d1b1bff0-35cd-3cf1-9809-64565b65ef10 | -12.0753 | -50.5759 | 2026-08-24 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 7dd3a13a-045f-3e2c-b082-354a5a5e70a2 | -6.6233 | -58.383 | 2026-08-24 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| be8a7317-2520-3300-92de-07a1c81e5567 | -12.075 | -50.5974 | 2026-08-24 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5ec121dd-9f39-36ff-ab86-efeb3ae9b54f | -17.6821 | -46.3908 | 2026-08-24 00:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1bec2cac-5e64-38bc-88a2-c53ea78576b6 | -22.9939 | -49.3597 | 2026-08-24 00:40:00 | GOES-19 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 72327454-0ae5-3c7d-bd97-d5c851f9d911 | -9.006 | -65.4 | 2026-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 655f4346-bc5a-37c6-9600-e99d8b127bc9 | -12.0938 | -50.6166 | 2026-08-24 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 895d4912-e2db-3086-b609-31bcde701408 | -23.0142 | -49.3779 | 2026-08-24 00:40:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| afa21870-742f-34b0-9b7c-146282ae4077 | -7.3788 | -45.8344 | 2026-08-24 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| f76dd1e6-5e36-3da7-a341-c39a0e416c77 | -5.78 | -57.5605 | 2026-08-24 00:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 5f8462a4-4fda-3702-8209-83ee84b65461 | -7.36 | -45.8361 | 2026-08-24 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 213.3 |
| 2095c571-9004-397a-86ea-9fc127f1f76e | -7.3791 | -45.8119 | 2026-08-24 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 254.6 |
| b39f4a83-842a-3a91-b527-a7af3d76e9ab | -8.797 | -62.8317 | 2026-08-24 00:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| f293dc18-ba69-36a7-9cf7-44bb6266306a | -12.0941 | -50.5951 | 2026-08-24 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |
| ac352cc2-b40a-310e-a2e3-8969ea46e30a | -8.9875 | -65.4006 | 2026-08-24 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 906d2d6d-0e6e-3cfd-9e72-0aec16df4542 | -7.3605 | -45.791 | 2026-08-24 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 157.5 |
| cf479b81-58e6-3207-a844-352b79153b65 | -8.9875 | -65.4006 | 2026-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| df229129-6e30-3c49-900f-9bccb42cef58 | -17.444 | -48.8199 | 2026-08-24 00:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| d979b75f-8add-3323-8d71-ff157547391a | -10.2198 | -36.2621 | 2026-08-24 00:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 45.7 |
| 20770ae5-58b2-37c7-acc5-6caf23f65ae4 | -12.0938 | -50.6166 | 2026-08-24 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| be6739de-3237-3193-8bd1-8056fe814c2e | -17.4236 | -48.8462 | 2026-08-24 00:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 24664a76-ed6b-3a6b-8cb9-599dc56f7355 | -9.0061 | -65.3813 | 2026-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.9 |
| c8fb7b8a-b2ba-3ac6-92de-1337d3a7421c | -6.3316 | -35.1619 | 2026-08-24 00:50:00 | GOES-19 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 78.8 |
| f1aadbd4-61c3-3932-abf7-c71eedfe8b8c | -10.2386 | -36.2857 | 2026-08-24 00:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 8ae1efee-c1a3-3a1b-85ba-93f1411a49df | -22.9932 | -49.3831 | 2026-08-24 00:50:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| 307751df-f798-376b-a3ac-a65143b947d9 | -9.006 | -65.4 | 2026-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| a9d0b0c9-ef86-33ca-a8c1-fb7f36c716e6 | -14.3365 | -51.7662 | 2026-08-24 00:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| ce6bbfef-afd6-3dc6-b9e0-fd2350e37a3d | -8.7785 | -62.8324 | 2026-08-24 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| c0444af0-7b43-3921-96e1-128b16219c6f | -7.36 | -45.8361 | 2026-08-24 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 269.9 |
| ad9aff3c-19df-3ee8-a0cb-2093b796233a | -7.3788 | -45.8344 | 2026-08-24 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.0 |
| 0bcf6e22-3221-3d8d-a803-578d9a3cc85e | -7.3793 | -45.7894 | 2026-08-24 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 818004d6-5a9f-3857-a02a-1023289cf81e | -10.2193 | -36.2892 | 2026-08-24 00:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 86.2 |
| b51fd7ee-8e47-384e-b389-ed4263ebf631 | -6.8491 | -52.505 | 2026-08-24 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 02425b76-1b74-3628-9c08-bf42eb78894b | -7.3791 | -45.8119 | 2026-08-24 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| 6f4536c8-8c35-35f7-8767-951cfc3b77e0 | -10.2391 | -36.2586 | 2026-08-24 00:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 39.2 |
| c02d89c0-61da-3c5f-99bc-1d094443fc46 | -17.4435 | -48.8425 | 2026-08-24 00:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 77.7 |
| b9c5cb10-04ad-3711-b30d-6e8deec7dcb4 | -5.78 | -57.5605 | 2026-08-24 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b620c0be-4491-34d7-94b4-0e80ef3995a1 | -12.0941 | -50.5951 | 2026-08-24 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 345b8e88-b55c-380a-937e-453340143c0a | -7.3603 | -45.8136 | 2026-08-24 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 395.0 |
| 3a101d2c-f4e8-3fe9-a869-bc70dde7d0f3 | -8.9876 | -65.3819 | 2026-08-24 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.1 |
| b93a2b4f-e6ab-3957-8614-e1e14943161d | -6.6233 | -58.383 | 2026-08-24 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 674fa83c-4537-3af2-8759-417d41caa986 | -6.6048 | -58.3838 | 2026-08-24 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 4b5aec03-a592-3170-a1cf-5320eeadc255 | -23.0142 | -49.3779 | 2026-08-24 00:50:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.7 |
| b82165fb-e48f-3fe5-864a-72dca0224c62 | -17.4241 | -48.8236 | 2026-08-24 00:50:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 132.2 |
| acbb28df-e472-3cd9-9b35-bb3fef2f4e3f | -17.6821 | -46.3908 | 2026-08-24 00:50:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 89cdf2c2-7776-3dde-8983-1f2c2d036861 | -5.6364 | -48.4091 | 2026-08-24 01:00:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 1d7410ca-83fb-34ff-bb20-1527fb0118da | -22.9932 | -49.3831 | 2026-08-24 01:00:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 59.9 |
| d19ff15d-3348-3061-97e0-53ba3b71006f | -9.0061 | -65.3813 | 2026-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| d0793ffa-7f4e-326c-a7f1-37705bff2e89 | -6.6048 | -58.3838 | 2026-08-24 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 64e1b20d-e50d-3f27-953d-e64a58431f54 | -23.0142 | -49.3779 | 2026-08-24 01:00:00 | GOES-19 | ÓLEO | SÃO PAULO | Brasil | 3533809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| 5957955d-c773-34bf-911a-0c1c3ff4b45a | -17.444 | -48.8199 | 2026-08-24 01:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 165.5 |
| cc50a06d-7ef6-317c-a511-2421de4ca741 | -9.4578 | -40.3392 | 2026-08-24 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 179.3 |
| 28100708-c8df-3da4-b1fc-4455d742119c | -7.3791 | -45.8119 | 2026-08-24 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 177.1 |
| db8f47d5-3a02-3cd4-b9d8-30897e4042b6 | -5.6178 | -48.4102 | 2026-08-24 01:00:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| d3391210-0ef5-3267-90ff-22be25609a6d | -17.4241 | -48.8236 | 2026-08-24 01:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 293.2 |
| 612a78b3-1b6b-30c5-8e37-74e48284408d | -9.4582 | -40.3143 | 2026-08-24 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 143.7 |
| 9c8944a6-0b68-3397-9e73-35ad8f3f0682 | -7.36 | -45.8361 | 2026-08-24 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 225.5 |
| b8d066cb-c549-378d-8d17-189245ab7349 | -7.3605 | -45.791 | 2026-08-24 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 8461ff95-1ed7-3413-8e94-a1aa3e3aaca6 | -8.9875 | -65.4006 | 2026-08-24 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| d52c8b73-3dff-3baa-8fbb-98f77ecf9525 | -7.3788 | -45.8344 | 2026-08-24 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 45d59d29-a242-3e90-82a0-9cfab30c4182 | -7.3603 | -45.8136 | 2026-08-24 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 371.8 |
| 3fd024f7-1489-3f63-b1d6-5531119ec1b7 | -6.6233 | -58.383 | 2026-08-24 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| c9be03f4-ded7-3af3-8a97-ec196ed41549 | -17.4236 | -48.8462 | 2026-08-24 01:00:00 | GOES-19 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 130.5 |


[Clique aqui para ver as próximas entradas](README6.md)
