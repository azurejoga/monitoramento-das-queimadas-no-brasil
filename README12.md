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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e88292c6-05ff-328b-842b-d3669c9bf44d | -7.23384 | -44.15716 | 2025-06-15 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c10eead0-7031-3e49-83cd-047cf5f0962d | -8.31169 | -46.20419 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1997fdf6-f879-3822-abe2-c22d667eccae | -9.42088 | -48.44143 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bb0d734-99bb-3f93-977f-ff1595c14cd6 | -9.41141 | -48.43734 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95250e04-85c7-306a-9fe8-6b62b795b955 | -9.40082 | -48.43215 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e89c568-6818-3740-9e28-d6b7f9f19977 | -9.41394 | -48.45156 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa7000e5-9ab6-3952-8ff4-97ec9a3f487e | -4.43453 | -46.11797 | 2025-06-15 05:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dab86cf-8146-384f-90d0-0337a143ef0c | -9.042 | -47.0175 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e74d2db7-d6a4-394d-941f-8888715140b0 | -8.30849 | -46.20271 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1121046f-bb57-36c1-9171-3609bab491b6 | -9.40565 | -48.42817 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e0ca97e-a34a-3ce9-b865-c9342135580e | -7.2301 | -44.16431 | 2025-06-15 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58d94e92-778d-36d1-9e8f-9dbbba10acca | -7.23791 | -44.15924 | 2025-06-15 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88f5cc24-eb15-3001-97da-3c8dfb5cf2d7 | -8.31414 | -46.20846 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 096f6ed3-2bc0-38fd-8400-f0cd4f8b9093 | -8.30538 | -46.20332 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46dff58e-2f65-3f3b-82d2-1b4071e4d775 | -9.67886 | -48.60944 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5105c4ef-d61c-3b7d-87cc-281df1fbec05 | -6.44555 | -45.72663 | 2025-06-15 05:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 540c9e24-b176-30d1-a684-5b3f8cb13fca | -8.37587 | -47.05559 | 2025-06-15 05:12:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6084b6ce-5759-3426-b940-971fcfa1dd19 | -9.4144 | -48.44797 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ca375d47-887e-3cfa-a9d5-4ac2d3b3626a | -9.41487 | -48.44434 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0dc00da4-1ade-30f1-9d04-f5c2b14f575b | -3.70599 | -53.71097 | 2025-06-15 05:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e40072c-8852-3f50-abc4-7283fd4e59f4 | -9.04143 | -47.02214 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13643ba3-02f3-336d-a3e7-9ff0d6e3fecf | -9.05232 | -47.91611 | 2025-06-15 05:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a73ebe0-8f6d-3c00-a368-f29dd9b28069 | -9.04086 | -47.02669 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fcb6b4e-9547-34a4-a7fb-c2da89e7d0ad | -9.40473 | -48.43545 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b70f3a0-75d0-3a13-a6d7-246b6e158968 | -7.23095 | -44.15767 | 2025-06-15 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 918bceaf-48b1-37b8-a712-33ec7ef001a5 | -9.05282 | -47.91216 | 2025-06-15 05:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5a3c8de-a320-3f76-bd5d-3ce5d7ad2dad | -8.36985 | -47.05511 | 2025-06-15 05:12:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f83ab168-ae65-3100-9074-3ccacdb05f00 | -3.70665 | -53.70937 | 2025-06-15 05:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8442a27-7419-325d-9af3-1d86d57922e5 | -7.08522 | -49.5992 | 2025-06-15 05:12:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fefc1b2-dcff-3594-af34-e9e597d43628 | -9.42041 | -48.4451 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| d05a3385-d3d6-374c-9b05-76ed977f53f2 | -9.40685 | -48.4293 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3653edba-2031-3cc2-8a44-83f1d3bcf1fb | -8.31479 | -46.20357 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a78b48e7-d724-3712-bf73-66a30fa9b4d8 | -9.41534 | -48.44067 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48e69464-4d4a-376d-929b-bda7e95e5f9a | -4.43514 | -46.11366 | 2025-06-15 05:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b205d80b-d6e1-3c94-893a-93fcd57b6852 | -8.96273 | -47.97166 | 2025-06-15 05:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47b2b64b-5df9-3749-a59c-f2bac832040a | -8.96842 | -47.97242 | 2025-06-15 05:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a965d59d-0133-3b97-94fd-9195b83d6e83 | -9.42501 | -48.45311 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 402d74af-09f1-34b8-86c7-37e3755b7dc2 | -9.05124 | -47.9159 | 2025-06-15 05:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff6c7413-0998-3b64-9b14-47e874f44aba | -9.41074 | -48.43256 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 601e0ac3-3721-336b-80e1-caccd6b25f60 | -7.23295 | -44.16373 | 2025-06-15 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f95a1060-2249-3ec9-b0cd-ebcc302ff49f | -9.03947 | -47.0246 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c6e49bc-b69e-3c88-92d3-0c2e25b6f175 | -9.41027 | -48.43623 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c464b6e2-5d25-328a-b699-a59a0ec0d6dc | -9.40519 | -48.43182 | 2025-06-15 05:12:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca2afbd9-0c19-3eb6-b95b-6a07bdd19f20 | -7.23876 | -44.15262 | 2025-06-15 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5bbbd43f-52f0-3fe9-aeb0-4ae959f4fe2c | -7.23471 | -44.15067 | 2025-06-15 05:12:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93670675-c2f8-3faf-8abb-f79dda8c7391 | -9.04007 | -47.02003 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58919299-ba61-3dbf-b436-390561f760bc | -6.44486 | -45.73162 | 2025-06-15 05:12:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33039993-085f-3bfe-96bd-3cda93513460 | -8.31799 | -46.20507 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 195b2141-a461-34cf-aef3-ef19f3c77531 | -9.03888 | -47.02909 | 2025-06-15 05:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94c47824-cdd4-3eea-9ad8-580255a84d34 | -9.05177 | -47.91196 | 2025-06-15 05:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f5cb66f-53a6-3bb7-84a0-f6a1265aa28b | -10.56788 | -52.01843 | 2025-06-15 05:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e75f2ca2-cb46-3300-944b-c3e43449178f | -11.00325 | -55.07441 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c99c7b14-deae-3157-aa81-f746e66e516d | -10.9144 | -54.76029 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0e868a7c-5bea-3289-96df-cd4e4270bde9 | -13.91898 | -54.64729 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef45a2d0-97da-33d9-bc9f-1c76f4b1d967 | -15.39582 | -47.87259 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ca9ff385-0f12-38de-ba4a-57643f448b4e | -14.03045 | -55.12801 | 2025-06-15 05:14:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cee30c3-d49f-317f-bee7-a2fa94af5e27 | -11.57306 | -47.87352 | 2025-06-15 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3584ba4-bbf0-39f2-aa29-fd83765925b3 | -11.00261 | -55.07875 | 2025-06-15 05:14:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 34a03f17-0233-3ce1-a80d-d268a254a02b | -13.91475 | -54.62104 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7b00e611-4c52-3a11-b9ef-7d9a201677ac | -10.85019 | -53.78432 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7afeaadb-2e35-3240-be95-57931de5979d | -10.91376 | -54.76475 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a966e871-b178-3bf3-b2a1-412d07b0b842 | -10.91132 | -54.75525 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58dfd6c2-b6ff-3134-ade8-e60bc1e536b0 | -13.91437 | -54.65173 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0fe4728f-4625-3fac-90d9-bba3b1715488 | -13.91756 | -54.65721 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b238856a-f226-340c-9cac-f5bc7192b7df | -13.91614 | -54.60831 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1031afc7-bf05-3e20-a19d-b69c69c4c8b5 | -13.91086 | -54.62042 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| deb5f85d-d648-39a2-8ef5-eab3a0434f10 | -10.62876 | -49.42811 | 2025-06-15 05:14:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18685539-d78d-3c9a-9d35-e4dc5a3a8402 | -15.40198 | -47.8737 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 814cd0df-88fc-3345-b740-f1c550a5ecb7 | -10.69494 | -57.64882 | 2025-06-15 05:14:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 893151f5-dfd9-3923-a356-43496be68094 | -13.9052 | -54.60409 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe9655a8-2317-39be-95f0-bf11e23c547b | -13.91546 | -54.61338 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 2395c730-1343-387f-9e4c-50d0db8e0ff5 | -13.91793 | -54.62666 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 685a0d1d-737b-39cd-8042-b0ca06e05d48 | -12.48522 | -58.46787 | 2025-06-15 05:14:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03db8a5e-2d37-3871-9282-1672727a09fe | -15.40918 | -47.86485 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a2c86e8-2d70-3c04-87ff-ee011c94ec30 | -12.08774 | -49.49035 | 2025-06-15 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab32143e-1df4-3fae-b838-da1827bf40f3 | -12.47135 | -58.46926 | 2025-06-15 05:14:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db242157-02ed-37d1-ba6a-8950f1b9b5e4 | -15.41603 | -47.85938 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a78f0329-4f10-3019-8bc4-7f6be36d7d3d | -10.51169 | -53.58309 | 2025-06-15 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e2ca6e6e-a379-3c0f-915a-ba5ae4a7137f | -13.90837 | -54.60979 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 8aebc332-7b25-31a1-8f2c-e9dc928c99b8 | -10.5057 | -53.5806 | 2025-06-15 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ea34bc11-ead7-374e-80c4-2823c5ac7aa3 | -13.92006 | -54.61173 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 65014729-e8f7-33a7-925c-aaece695caa5 | -13.92258 | -54.61961 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 85b0479f-e9fd-315d-963e-503c42dbba91 | -13.91868 | -54.61901 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 50f7fbb0-57e0-316b-a7e4-4af8c67fb0d6 | -13.28988 | -57.07117 | 2025-06-15 05:14:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d13de1ae-e33d-3b31-a21f-1d1c632f64de | -13.94989 | -54.44744 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e91e929-dba8-32ef-a4f9-36fa14d0af67 | -10.85485 | -53.77987 | 2025-06-15 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0276fb3b-1944-32a7-853a-75dd40a60d50 | -14.03181 | -55.11848 | 2025-06-15 05:14:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0675e75-6f22-3418-870d-f8671e2691c2 | -13.92183 | -54.62729 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 0949986e-e47d-388d-9fd6-842b875c9a6e | -12.09311 | -49.49104 | 2025-06-15 05:14:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31e30a6d-75f6-35e2-8c65-7133d03dcd4b | -13.9265 | -54.62013 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78379380-52dd-3fd5-8356-1fdc3f453e66 | -15.39995 | -47.85294 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e939e19-8a70-3b2d-8a76-fc7e279315a0 | -15.40302 | -47.88206 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 511f0829-b410-3c8b-8c1d-5d6019782190 | -14.54204 | -59.87 | 2025-06-15 05:14:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3829c0f6-89a1-31ec-a9ac-4ccbe124d6b3 | -12.47857 | -58.46679 | 2025-06-15 05:14:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46e63f7e-14a8-34b2-a259-6ae5b5cc97d2 | -10.45472 | -47.951 | 2025-06-15 05:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 952beb9b-2564-3f62-b706-2373cc0c71c1 | -14.54537 | -59.87057 | 2025-06-15 05:14:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f8b6150f-b3cf-33f1-9525-7a6b63271227 | -16.28593 | -52.93157 | 2025-06-15 05:14:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6465f448-71e4-3dff-80aa-46fc85127731 | -11.57619 | -47.87213 | 2025-06-15 05:14:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5fa4c96-d460-3110-8f11-ad94c6dffd6e | -13.90057 | -54.60858 | 2025-06-15 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 776adcf4-f3c0-3731-9521-4b690c67a9a0 | -15.40772 | -47.87891 | 2025-06-15 05:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README13.md)
