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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e76f72c9-5159-3937-a429-f026e546e76e | -13.5844 | -51.8632 | 2026-09-14 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 47316877-7ef8-301e-9e1e-60572890f654 | -7.8715 | -54.7016 | 2026-09-14 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 07a314b3-e539-33e3-8209-4305cafe6136 | -13.2867 | -51.3046 | 2026-09-14 16:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 818.7 |
| cb9d6d2f-2d96-33a1-9b58-ed906106b519 | -1.7316 | -54.9518 | 2026-09-14 16:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| b4bed248-2250-3444-812d-9653228699d2 | -6.0925 | -57.6847 | 2026-09-14 16:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 30a2a967-ac90-3f90-8a1b-4b4729091000 | -13.5526 | -51.4629 | 2026-09-14 16:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| be1d8a51-733c-3142-aa5a-efdc3732117a | -3.3638 | -61.2904 | 2026-09-14 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8aa49f77-ee9a-3317-b17e-fa4db77c183a | -11.8365 | -50.0028 | 2026-09-14 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| e3e823b9-79a3-3a08-9691-3c513c6d4596 | -10.5484 | -51.2945 | 2026-09-14 16:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 76309277-f1ba-3647-9f5b-0da3057feeb1 | -2.6602 | -57.5119 | 2026-09-14 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| b339aca6-1f48-31dd-90e2-25bb222ebe39 | -9.3951 | -50.1121 | 2026-09-14 16:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 102bb1c2-064a-3935-a06c-7a061b1463d8 | -10.7532 | -46.2573 | 2026-09-14 16:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 72ac2710-67e9-3f34-9245-969de002733d | -10.7839 | -50.6346 | 2026-09-14 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 386bdbc9-edeb-3f64-aa84-3bc80953f8c8 | -3.1632 | -61.1805 | 2026-09-14 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 357e2666-dcd0-3f6e-a377-f894bcefb422 | -10.5667 | -51.3349 | 2026-09-14 16:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 44e1abb1-3543-31b4-97cd-21383d71a4fd | -3.3638 | -61.2904 | 2026-09-14 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 141dcd67-1f1f-3e36-ab14-c3074d5375e4 | -3.314 | -59.3706 | 2026-09-14 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 113.4 |
| b39506ee-f2f2-3268-b5cf-dfea06842aaa | -11.5095 | -50.2559 | 2026-09-14 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 4651b5aa-05ed-3a5d-b5eb-e27c4c98069f | -10.7463 | -50.6172 | 2026-09-14 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 37f37207-4171-3381-bc88-f29f769bd83c | -3.4003 | -61.3087 | 2026-09-14 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 7c13aef0-5858-3f36-823f-05703c08bf14 | -13.5844 | -51.8632 | 2026-09-14 16:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 5faaf2f9-e601-36a7-b474-35007c93a6d3 | -6.1111 | -57.6645 | 2026-09-14 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 64583aba-b8d6-3e68-a451-30815e9f2b2a | -2.6968 | -57.5112 | 2026-09-14 16:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| d4a99307-7e33-320e-b281-329796d0113a | -10.2929 | -45.2932 | 2026-09-14 16:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 94.0 |
| b7904c57-8e2d-3ee8-8819-2ea00a896385 | -3.4186 | -61.3084 | 2026-09-14 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 9d93cd71-7e0b-3823-9e1f-f5ba970b0c4b | -13.5526 | -51.4629 | 2026-09-14 16:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 9fe09a7d-5b11-3beb-8938-0d529c6b2103 | -10.7274 | -50.6192 | 2026-09-14 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 242.9 |
| fb0728e8-805a-3942-ae62-4ac738f17fa8 | -13.2867 | -51.3046 | 2026-09-14 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 334.5 |
| 63569dfa-cc6b-3fad-9f23-b43cf328b981 | -13.3059 | -51.3022 | 2026-09-14 16:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 965bbc3f-037c-3af5-8d29-e5d143d64b61 | -7.1012 | -42.1088 | 2026-09-14 16:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 267.0 |
| ff78010d-af02-35a4-9b51-1d911c86213f | -10.8028 | -50.6326 | 2026-09-14 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 5ed07e78-0b05-30db-9ae5-d15fc35afbf9 | -3.1816 | -61.1045 | 2026-09-14 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 2b75495a-5092-3a7c-b381-3acbe12a4390 | -10.7722 | -46.2549 | 2026-09-14 16:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 79deddb2-6ea4-3ce6-b012-7f2dd8cd08b8 | -10.7084 | -50.6212 | 2026-09-14 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| b107e898-8bbb-357e-9a35-3b0ab5be96a8 | -3.3639 | -61.2715 | 2026-09-14 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bb89c1fb-b359-3e66-9600-236d89c86bfe | -10.5481 | -51.3156 | 2026-09-14 16:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 9ba9c142-28f8-3e72-9928-552540d59d2f | -3.0904 | -61.0682 | 2026-09-14 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 5581655e-c8a4-39f2-8864-4c196e0b712f | -12.0273 | -49.9799 | 2026-09-14 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 184.4 |
| 1d61e9fd-8f05-3d11-b032-b1a75d2b6624 | -10.81 | -46.29 | 2026-09-14 16:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b0e30fc-0a51-37ac-94e3-0f2956c19818 | -10.31 | -45.3 | 2026-09-14 16:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f82d268d-e54d-3c5a-8d5a-1272564a68b0 | -10.34 | -45.31 | 2026-09-14 16:15:00 | MSG-03 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1ed7192-2b36-3ab8-b300-6c28ff9129ac | -10.84 | -46.29 | 2026-09-14 16:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa0b72d2-2de0-393c-946c-a9e283f5a637 | -9.3946 | -50.1548 | 2026-09-14 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| eec3fb44-3351-3ec7-b11c-044fbe446d98 | -10.7274 | -50.6192 | 2026-09-14 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 154.1 |
| f144716d-9ea1-3548-ad7a-303c275ba2e3 | -10.5667 | -51.3349 | 2026-09-14 16:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| feabaf2c-d6f3-3274-8ac1-79626e7e8d5b | -10.7084 | -50.6212 | 2026-09-14 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 08b00427-60fe-38e4-b6d7-140d85f61434 | -13.5526 | -51.4629 | 2026-09-14 16:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 56c2fbdc-0265-3a53-b545-216ee6967935 | -3.4186 | -61.3084 | 2026-09-14 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a92bdc87-f8a3-3428-aca6-342e0ca90cac | -10.7839 | -50.6346 | 2026-09-14 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 194.0 |
| 3e6f3ab2-ee50-3521-8e81-b199c90abcab | -6.1111 | -57.6645 | 2026-09-14 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 174.4 |
| af1cbdc0-2573-3983-b7c2-3e5f4150c7ec | -2.6968 | -57.5112 | 2026-09-14 16:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 226c17a1-4b12-3a81-a8d3-7cc2e7a8e650 | -13.2867 | -51.3046 | 2026-09-14 16:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 43ea4cbd-a5ce-3d8b-a11f-7a98d53f237b | -13.3059 | -51.3022 | 2026-09-14 16:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7e906199-f21a-3068-9b96-64fb9637b71b | -9.3948 | -50.1334 | 2026-09-14 16:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 40e6d88c-4f78-3640-ab08-93fe0e2b4527 | 1.3634 | -56.1031 | 2026-09-14 16:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| d19303c0-3761-3cc6-949a-b11cbdb48b00 | -3.3639 | -61.2715 | 2026-09-14 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 16f35e19-d94f-3edc-95f2-6899e9296dac | -13.3185 | -51.7051 | 2026-09-14 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f49406e0-6b65-3b80-8e79-cdfb5d16c7a7 | -13.5526 | -51.4629 | 2026-09-14 16:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 33d2d4cc-e6ca-32ac-9c22-89999c894df7 | -6.1111 | -57.6645 | 2026-09-14 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 9f7a54ef-ccfa-3ddb-aa2d-4b13a189999f | -13.3059 | -51.3022 | 2026-09-14 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4fc4a22f-2445-3cdf-8745-b4b1d0a56b8c | 1.0951 | -50.957 | 2026-09-14 16:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 8efb5057-d396-3a66-8688-d0959c556845 | -10.5667 | -51.3349 | 2026-09-14 16:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 2cfaefdf-64a5-3a03-aad3-82dd0d482fb8 | 1.3634 | -56.1031 | 2026-09-14 16:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 5cebfeb7-c314-3a0d-8675-9726d8c58210 | -3.4186 | -61.3084 | 2026-09-14 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 77b86e7c-ed36-3a86-a7be-d3331cbff893 | -2.6968 | -57.5112 | 2026-09-14 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 64da6042-63e2-3a7f-9a9b-bde4651498e5 | -2.6601 | -57.5507 | 2026-09-14 16:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 56cbc727-27db-3789-9ccf-6f548e6c8601 | -3.3639 | -61.2715 | 2026-09-14 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 100.5 |
| f2d3d939-077f-3e13-aae4-b2debe9e7e41 | 0.1747 | -51.4805 | 2026-09-14 16:30:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 95.0 |
| ac0fd2e7-0dd7-3b95-b5ef-877a543d330f | -13.2867 | -51.3046 | 2026-09-14 16:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 205.7 |
| fe2f3dcd-d92f-3ed1-86f3-d77d034c434f | -8.5815 | -44.4398 | 2026-09-14 16:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 188.3 |
| b1606da9-04ba-387a-86d4-d2c234574839 | -11.955 | -49.7295 | 2026-09-14 16:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| a764e018-1c68-336c-90a7-472e3d943bf1 | -13.2867 | -51.3046 | 2026-09-14 16:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 156.9 |
| ce283a81-eeb0-3d00-b261-cc8499b81c23 | -9.3765 | -50.0925 | 2026-09-14 16:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b8b55635-b43d-3170-8058-386b69efb5be | -6.1111 | -57.6645 | 2026-09-14 16:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 29560d4e-e7fb-3a31-955c-e5f970f8403a | -2.6601 | -57.5507 | 2026-09-14 16:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 6bb6c73d-5b20-3b9d-8598-6d221d41f561 | -13.3251 | -51.2997 | 2026-09-14 16:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| b94bbc60-4ee6-3ce9-b0e6-5759922f9edf | -13.5526 | -51.4629 | 2026-09-14 16:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 238.1 |
| ecfd0e6f-8078-3d13-b0b4-9e829d7daf56 | -13.3059 | -51.3022 | 2026-09-14 16:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.4 |
| e0abafd9-c149-31ab-9a15-a26b69d68c39 | -9.3763 | -50.1139 | 2026-09-14 16:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 111.4 |
| bc657ddd-0903-3197-9fa3-6b1fc507ffef | -13.2867 | -51.3046 | 2026-09-14 16:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 237.1 |
| 83bc74b2-b877-3e49-9aac-a2956c54ce96 | -7.1012 | -42.1088 | 2026-09-14 16:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 487.2 |
| f87196af-7ecc-3f51-8517-43d540a826a7 | 2.316 | -55.9328 | 2026-09-14 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 6b07fb70-886c-3812-ae1b-2d3aecf1c02c | -6.1111 | -57.6645 | 2026-09-14 16:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 176.1 |
| 51e696f5-78c9-34c5-8231-1ee6926734fc | -2.6786 | -57.4921 | 2026-09-14 16:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| cb52f576-a7e7-3801-822a-a58f639e7e91 | -9.376 | -50.1352 | 2026-09-14 16:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| f1198418-0ef2-3d0b-b52c-cabe6b10102b | -13.5526 | -51.4629 | 2026-09-14 16:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 6230cd64-6202-3af3-9ef7-4a6260f1f011 | -13.3059 | -51.3022 | 2026-09-14 16:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 390d4918-2a49-39f8-8388-f303ad451aec | -7.12 | -42.107 | 2026-09-14 16:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 169.0 |
| 8d4f86a9-390e-3054-9927-83208ed438f7 | -9.3758 | -50.1565 | 2026-09-14 17:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 6a5fc0ec-ce78-3baa-b763-ac63497901b6 | -9.3755 | -50.1779 | 2026-09-14 17:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 181.8 |
| 92f5ad53-c012-3597-9bfc-8d8c7b20692d | 2.316 | -55.9328 | 2026-09-14 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 41988685-5581-3382-8e51-6e1c8a9f1cf0 | -3.4374 | -61.0812 | 2026-09-14 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| b2d8d8f5-f768-360a-acf4-e6334ddd2135 | -6.1111 | -57.6645 | 2026-09-14 17:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 7a7501c8-e7aa-3407-b8f9-b621eab2bf85 | -2.6786 | -57.4921 | 2026-09-14 17:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| e7488698-7930-3954-acf6-e150c92d01aa | -1.3007 | -49.1464 | 2026-09-14 17:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8ec73158-d4ae-3ded-a9f8-1c1a0b22a6f9 | -6.1111 | -57.6645 | 2026-09-14 17:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| b0a39bd9-fb2c-3fa7-a0b6-5feaf560f530 | -9.8511 | -48.3397 | 2026-09-14 17:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| b3aa9724-fdef-3ebc-8f61-c152e4f52769 | -13.3247 | -51.3211 | 2026-09-14 17:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 67bb2755-376a-35c9-81dc-03a7c3bef334 | -11.2488 | -54.1378 | 2026-09-14 17:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1ef7864e-8f62-3a29-93f0-05217cb1c89e | -10.69 | -54.2 | 2026-09-14 17:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README95.md)
