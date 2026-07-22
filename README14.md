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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cffe530f-8cae-3368-b8bd-27ed0b5b5f24 | -13.396 | -51.653 | 2026-07-22 14:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 75d93c0e-513d-3986-a6a1-3b8c13b46835 | -13.3169 | -54.3221 | 2026-07-22 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 17b6dbd4-38b9-3638-8e56-4c1b7dd72726 | -13.3363 | -54.2993 | 2026-07-22 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| a981b579-af47-384f-8cec-6787582f9456 | -12.533 | -48.2555 | 2026-07-22 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 2faeb76a-600c-35a5-a030-d9ce2e106fde | -13.3361 | -54.32 | 2026-07-22 14:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 150.3 |
| 2b484add-1866-3d60-ae91-7535fc3c9a56 | -12.533 | -48.2555 | 2026-07-22 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| ba60ce7e-b177-3a87-a8ee-8e38738ce82a | -12.5138 | -48.2581 | 2026-07-22 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 9eb64a92-4cf9-39bd-a5b3-93d75618c03a | -11.7768 | -61.3247 | 2026-07-22 15:00:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 101.3 |
| ec4b02fd-b752-37ac-8b55-8d467b5fe141 | -10.8244 | -50.4385 | 2026-07-22 15:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6ff31af8-3601-32a7-9b74-8fa604fb6174 | -6.03 | -43.8727 | 2026-07-22 15:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 174dca62-2d4c-36cd-8fa5-ebdf343c7b12 | -12.5334 | -48.2333 | 2026-07-22 15:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 78f0f29a-7842-34ba-9b0d-efdfcc1083fe | -12.533 | -48.2555 | 2026-07-22 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 7632396a-9610-3ac2-a7d6-be106b0f62ce | -13.396 | -51.653 | 2026-07-22 15:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| b8756fc2-cb4f-3400-8027-5a47f2149f12 | -11.7768 | -61.3247 | 2026-07-22 15:10:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 122.1 |
| d06eb787-b5ce-32ec-a7d7-22a144ac86b7 | -14.332 | -53.1846 | 2026-07-22 15:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6efae622-5ca8-3aeb-a289-ad36e7ac3bd7 | -10.8244 | -50.4385 | 2026-07-22 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 6b6d1f31-9d96-37b2-a8f9-040674a733fb | -12.5334 | -48.2333 | 2026-07-22 15:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 93c67f40-793a-3c6c-bd5b-ed3d281b5a1c | -17.5748 | -47.4996 | 2026-07-22 15:10:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| decc306f-e0af-36d7-af3d-dda9ed6e6363 | -12.5334 | -48.2333 | 2026-07-22 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 1c2cf129-dbd9-3e88-9319-728a8240aefe | -13.396 | -51.653 | 2026-07-22 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |
| fe323c22-84d6-3035-bba1-61c12c6caad1 | -13.4152 | -51.6506 | 2026-07-22 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 11d14f75-8807-3d6c-b328-eb93667af6ec | -10.9216 | -50.2571 | 2026-07-22 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| ed7f6770-87fb-35cf-be82-c49c0c27db96 | -12.533 | -48.2555 | 2026-07-22 15:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 041ee07a-7e6f-36e8-9d42-217a97e98118 | -13.3169 | -54.3221 | 2026-07-22 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 899171b3-87f2-34af-b8ae-c209d049e150 | -14.332 | -53.1846 | 2026-07-22 15:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| b440597e-b23b-327f-b403-e7fe715b1ad1 | -10.8244 | -50.4385 | 2026-07-22 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 580ca514-34c7-3402-9bd0-02890c760411 | -13.3172 | -54.3014 | 2026-07-22 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7a95c335-1882-3d9d-9a0c-260bf07cc8d3 | -11.7768 | -61.3247 | 2026-07-22 15:20:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| c4bde164-2fe5-364c-8a58-2d64d310d19d | -13.3363 | -54.2993 | 2026-07-22 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| b1007970-8566-3c17-819b-70509799954f | -13.3363 | -54.2993 | 2026-07-22 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.6 |
| d2cc3453-6fa3-3eee-a16f-7345242bf531 | -12.533 | -48.2555 | 2026-07-22 15:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 3467c250-55d4-37eb-a523-aad5548563ff | -13.396 | -51.653 | 2026-07-22 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 91eaad6d-d13c-3f55-8da8-cc5786dfb3c2 | -14.332 | -53.1846 | 2026-07-22 15:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 105.1 |
| d339b9f8-1498-3c74-96de-4260d96f1808 | -9.1234 | -61.0844 | 2026-07-22 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 63710d25-5741-310b-8d3a-70bbf15ecdb1 | -12.3215 | -53.2686 | 2026-07-22 15:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7e0290e0-b4be-3225-9a06-352f7df803b8 | -11.7768 | -61.3247 | 2026-07-22 15:30:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 0748999e-d792-3d81-8f0c-0c9f421323b9 | -13.4152 | -51.6506 | 2026-07-22 15:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 141.6 |
| f29e6983-a01d-3e64-9061-379dccdca126 | -12.3212 | -53.2894 | 2026-07-22 15:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| b79cfb28-d975-3ffa-a6d1-d5182d71c499 | -12.5334 | -48.2333 | 2026-07-22 15:30:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| facb8bc4-6ab2-3f4c-a7d1-ff99f69682dc | -13.4152 | -51.6506 | 2026-07-22 15:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 505f1ac3-7c75-37b8-9486-825ddf3b8088 | -11.7768 | -61.3247 | 2026-07-22 15:40:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 5edde6f7-bc01-3199-9b23-798790c4ad37 | -13.3555 | -54.2973 | 2026-07-22 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 164cbd3a-e4a6-3bae-b084-e38c0e347492 | -10.9026 | -50.2591 | 2026-07-22 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 2fbe85a3-2043-3a4b-8cee-d6d5f46c3c9c | -12.3215 | -53.2686 | 2026-07-22 15:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e306675c-14bc-3df5-a1fd-a4adae2d9130 | -17.5748 | -47.4996 | 2026-07-22 15:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 38a02e07-88e9-3877-a7c4-3aa7399244ee | -14.332 | -53.1846 | 2026-07-22 15:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| d53844e5-61b5-36db-9b69-902de9927dac | -13.3169 | -54.3221 | 2026-07-22 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 45870b71-aed6-309f-8600-0e7d149f8b24 | -13.3172 | -54.3014 | 2026-07-22 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 9f4f2b69-f7f0-33d2-bb3a-3ee3f38145f8 | -13.3363 | -54.2993 | 2026-07-22 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.6 |
| 61541f67-6cbd-35b7-b688-f31874c01109 | -12.3212 | -53.2894 | 2026-07-22 15:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b18b843a-cb0f-368c-b703-d2fa74082436 | -10.8244 | -50.4385 | 2026-07-22 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.6 |


