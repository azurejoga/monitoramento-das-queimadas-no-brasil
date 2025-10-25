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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acf412ab-a1f2-3e37-990f-155f1f55f22f | -21.92636 | -46.52071 | 2025-10-25 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 4442d06f-680a-38fe-b592-3a2dd1e09f6d | -21.92529 | -46.50446 | 2025-10-25 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0c7226ba-d80f-3c35-9fb3-0f55dc3b4e07 | -21.9009 | -46.5521 | 2025-10-25 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f237d75e-6750-3e50-9c72-1ac5853a2ff8 | -24.88721 | -49.6459 | 2025-10-25 04:23:00 | NOAA-20 | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 264f529d-221f-3235-9f2e-6c15f58c6da6 | -24.12753 | -49.69523 | 2025-10-25 04:23:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ece88a61-f0a1-3d0a-ac25-a5d0c549632b | -21.91844 | -46.5273 | 2025-10-25 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 26d27642-d267-3ee1-a651-79414abda01f | -22.13767 | -55.28212 | 2025-10-25 04:23:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 786a7568-280a-3f61-ba8f-8de7698f21e7 | -23.89123 | -51.24174 | 2025-10-25 04:23:00 | NOAA-20 | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cbd4b8af-89b8-347b-af13-e1203b00c0f1 | -21.7886 | -46.17207 | 2025-10-25 04:23:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e80b900f-4481-3643-b019-71c474b68a4d | -21.92693 | -46.51681 | 2025-10-25 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 686a5121-9886-3657-a45f-53ed5e5ca79c | -23.30988 | -47.99923 | 2025-10-25 04:23:00 | NOAA-20 | QUADRA | SÃO PAULO | Brasil | 3541653 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0a797be6-100b-34c2-9e10-29be5bc2f844 | -23.13493 | -47.3382 | 2025-10-25 04:23:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 762e6c30-073e-3f48-b048-7e3a15b89771 | -21.92133 | -46.50776 | 2025-10-25 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d8215ed6-290d-314e-b0fa-89c4560b407c | -22.22615 | -53.34947 | 2025-10-25 04:23:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| f4ea8b07-3d7e-343e-af8e-982d643e4468 | -22.83205 | -51.35394 | 2025-10-25 04:23:00 | NOAA-20 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 44c9c9c7-c877-3b26-aae0-4dd60d42b807 | -24.60722 | -48.45388 | 2025-10-25 04:23:00 | NOAA-20 | IPORANGA | SÃO PAULO | Brasil | 3521200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 79da2b9d-27f1-3d3f-b251-841c11967d80 | -24.42262 | -50.76774 | 2025-10-25 04:23:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bb3b2409-828f-3fec-aabe-e25d73b066ac | -23.40948 | -49.67995 | 2025-10-25 04:23:00 | NOAA-20 | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0a07f896-cadc-341a-be10-13c93f51371a | -22.18549 | -44.1301 | 2025-10-25 04:23:00 | NOAA-20 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 19c5e4e5-5ed5-3761-9ba4-eab42e8f0cd0 | -23.34391 | -47.17281 | 2025-10-25 04:23:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 41785bbe-088d-390e-9b3c-061b3cd5db0f | -23.21074 | -45.9529 | 2025-10-25 04:23:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61089407-13ae-371e-ba92-1b59f3ba332d | -22.28953 | -46.83237 | 2025-10-25 04:23:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ba4b0a8-bbad-3d13-813d-afdc4fd6baf3 | -21.91447 | -46.53064 | 2025-10-25 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a2c6cf5f-a18a-32a1-880a-ae85fea36bd3 | -23.39138 | -51.12597 | 2025-10-25 04:23:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5552badb-58de-30fb-b1e3-314894580261 | -25.09685 | -52.3241 | 2025-10-25 04:23:00 | NOAA-20 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 8ec14888-96b1-34d2-8a1d-894999968db6 | -23.40154 | -49.68636 | 2025-10-25 04:23:00 | NOAA-20 | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5f84ce2d-1292-3853-9a9c-8cbd839b6863 | -22.02048 | -46.47546 | 2025-10-25 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c61ebc54-856e-3daa-b563-36207c1364cb | -25.03962 | -49.71453 | 2025-10-25 04:23:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 26d59e36-0e70-38a9-a06f-89a1da938412 | -22.22487 | -53.3513 | 2025-10-25 04:23:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| cf3e3ec0-d5d5-3975-9490-c31d658e1f2f | -24.80899 | -50.22641 | 2025-10-25 04:23:00 | NOAA-20 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e376ef27-4c94-3e8d-af10-76a02199f8f7 | -22.14208 | -55.28313 | 2025-10-25 04:23:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19b278ff-1721-3400-954b-a37cd3702c17 | -21.91901 | -46.52343 | 2025-10-25 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| f5147957-4d08-365d-b8ca-04f66e1c22e6 | -22.3188 | -52.26576 | 2025-10-25 04:23:00 | NOAA-20 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 41752581-deeb-3e06-b2a4-30de8a13a452 | -24.81234 | -50.22709 | 2025-10-25 04:23:00 | NOAA-20 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a14d331f-7b32-3ba7-8170-36dd8cb0e9cd | -21.92471 | -46.50837 | 2025-10-25 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1cafa187-c56e-3035-b870-26c95c8342cb | -21.7888 | -46.17317 | 2025-10-25 04:23:00 | NOAA-20 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 49c38a0b-9373-3f39-8872-8de6ee7087d3 | -22.20237 | -46.92044 | 2025-10-25 04:23:00 | NOAA-20 | ESTIVA GERBI | SÃO PAULO | Brasil | 3557303 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f035d9c4-9622-3429-911b-a176b48a0ec6 | -22.28616 | -46.83181 | 2025-10-25 04:23:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22a26f49-5429-346e-8074-6264160f4bf5 | -22.32457 | -52.26415 | 2025-10-25 04:23:00 | NOAA-20 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bdb8de09-812a-321d-8c26-8445d4d4cf4a | -22.32369 | -52.26888 | 2025-10-25 04:23:00 | NOAA-20 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a0ba59ab-5f84-3b02-a4de-d2244d61e920 | -20.50652 | -54.58214 | 2025-10-25 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d74d79e-d814-3798-a9ac-ae9956cf3a74 | -21.92355 | -46.51621 | 2025-10-25 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| aa43398b-3c93-3547-aa95-206a91b737d5 | -23.80862 | -51.0687 | 2025-10-25 04:23:00 | NOAA-20 | TAMARANA | PARANÁ | Brasil | 4126678 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 90858c71-b0cd-3a6f-86b1-e953ad764f78 | -23.3982 | -49.68571 | 2025-10-25 04:23:00 | NOAA-20 | CARLÓPOLIS | PARANÁ | Brasil | 4104709 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 457c7e6e-dc38-3e38-9032-65f2806e9964 | -23.8947 | -51.24246 | 2025-10-25 04:23:00 | NOAA-20 | MAUÁ DA SERRA | PARANÁ | Brasil | 4115754 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d2ff1726-c9a0-3c32-985d-1fe7c2e74e6c | -21.92297 | -46.52013 | 2025-10-25 04:23:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 42ad6b0a-0c3e-3e44-b06a-3bd62b51fc21 | -26.1729 | -51.73484 | 2025-10-25 04:23:00 | NOAA-20 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| bf33630c-85dd-329a-b6b8-4940be0ff0e6 | -22.14834 | -55.27489 | 2025-10-25 04:23:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47ca46cb-cbff-3a3b-a1ab-d9800975f3ca | -23.13363 | -47.33485 | 2025-10-25 04:23:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c8a13700-5129-3488-b6cf-ad8f7c6525a7 | -22.79909 | -46.43357 | 2025-10-25 04:23:00 | NOAA-20 | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6b6cfc60-ae51-3f1c-851a-737aecda83fb | -20.53077 | -54.59755 | 2025-10-25 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05c959ff-69a9-37fa-89db-9f54e1e71e24 | -22.82852 | -51.35325 | 2025-10-25 04:23:00 | NOAA-20 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9e630644-d536-3d6e-bb9e-a93003a5dabf | -22.32087 | -52.26342 | 2025-10-25 04:23:00 | NOAA-20 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| d1f80471-aa3c-3eb6-a055-bddd2d6dee6c | -23.1355 | -47.33438 | 2025-10-25 04:23:00 | NOAA-20 | SALTO | SÃO PAULO | Brasil | 3545209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b0b1ac1-c953-3a0f-92ff-1cc1139549ad | -21.91787 | -46.53117 | 2025-10-25 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7c10059e-e871-31dd-8a8b-dcfd8036c575 | -25.19342 | -50.40933 | 2025-10-25 04:23:00 | NOAA-20 | TEIXEIRA SOARES | PARANÁ | Brasil | 4127007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 20d8d60b-a4d5-3b04-bbe3-4bc330ddfb25 | -24.80834 | -50.23032 | 2025-10-25 04:23:00 | NOAA-20 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f4c0a508-0989-39ab-a4ec-301f56a1c660 | -24.21946 | -54.27341 | 2025-10-25 04:23:00 | NOAA-20 | GUAÍRA | PARANÁ | Brasil | 4108809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fad0a0a8-6be5-3178-bbe0-400e2d024d4c | -22.31999 | -52.26814 | 2025-10-25 04:23:00 | NOAA-20 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.9 |
| 01f1047a-a89f-3139-9115-d12a7f561674 | -23.62474 | -46.49663 | 2025-10-25 04:23:00 | NOAA-20 | SANTO ANDRÉ | SÃO PAULO | Brasil | 3547809 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 389fc695-7dd1-3b7c-9b4a-8f6a30a7ebe9 | -23.505 | -46.52691 | 2025-10-25 04:23:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8694166d-5b85-364c-8121-2a81d7bf072a | -22.31964 | -52.26103 | 2025-10-25 04:23:00 | NOAA-20 | TEODORO SAMPAIO | SÃO PAULO | Brasil | 3554300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| f95d2e8f-00de-3b13-a342-43286c2678f3 | -23.29908 | -46.64678 | 2025-10-25 04:23:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ea065070-662d-3f10-be49-7779aa28a156 | -23.12232 | -50.20766 | 2025-10-25 04:23:00 | NOAA-20 | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 60f942e7-00c2-3c9d-bd1b-21116f2aaed6 | -22.14742 | -55.2795 | 2025-10-25 04:23:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f15b3983-ce96-396c-80dd-904da4d57129 | -24.13149 | -49.69203 | 2025-10-25 04:23:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 94728936-dbc6-38c6-b676-1df31510a34c | -24.98451 | -51.524 | 2025-10-25 04:23:00 | NOAA-20 | TURVO | PARANÁ | Brasil | 4127965 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7e61e967-d69c-3e7e-a691-e21ef09f503d | -20.55941 | -54.65867 | 2025-10-25 04:23:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e17e749-d17d-3661-9dbd-325e3bf0370b | -21.91563 | -46.52285 | 2025-10-25 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 58a32594-ba5b-35d6-956b-210c9031809e | -23.34449 | -47.16894 | 2025-10-25 04:23:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c88dd073-15d5-303b-9f4b-77f6276d586d | -23.39202 | -51.12897 | 2025-10-25 04:23:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| c1d25b9b-4641-351e-9224-e2a1316dcae0 | -23.34056 | -47.1722 | 2025-10-25 04:23:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd58c127-7a5d-3674-98be-55328029892f | -21.95797 | -46.1624 | 2025-10-25 04:23:00 | NOAA-20 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f1d45069-2a64-3cec-ae57-5bc606ca1a9f | -22.2901 | -46.82853 | 2025-10-25 04:23:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fe46ffb-d061-329a-a68e-214a5ffb6c5f | -24.60663 | -48.45769 | 2025-10-25 04:23:00 | NOAA-20 | IPORANGA | SÃO PAULO | Brasil | 3521200 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b0b21c94-04c6-37d9-b724-24b4b956527d | -23.40499 | -46.42078 | 2025-10-25 04:23:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c27a51a4-8e93-3ef7-8bc9-401a78e1bf31 | -26.39871 | -49.90952 | 2025-10-25 04:23:00 | NOAA-20 | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 964b4e98-9e4b-313f-a5d3-3014fb463da1 | -21.91505 | -46.52674 | 2025-10-25 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e351ae1f-c488-35c8-839a-a624cc739162 | -22.83558 | -51.35463 | 2025-10-25 04:23:00 | NOAA-20 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| bd336368-2d83-3086-9fd9-a160c34fb052 | -24.79274 | -49.17787 | 2025-10-25 04:23:00 | NOAA-20 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b52565b7-cad7-3bf9-bac1-fc86b5aaaf29 | -21.88728 | -45.26707 | 2025-10-25 04:23:00 | NOAA-20 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 29ea3733-e157-35ba-b7fc-dadcdc0523e2 | -22.58191 | -44.2769 | 2025-10-25 04:23:00 | NOAA-20 | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9a26bbb6-6304-31f3-a8d4-9226770649a3 | -24.30743 | -49.42716 | 2025-10-25 04:23:00 | NOAA-20 | SENGÉS | PARANÁ | Brasil | 4126306 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 37bb3b9c-ad0b-3f80-a140-4b0c92aa17b0 | -21.9224 | -46.524 | 2025-10-25 04:23:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 31717178-aabf-3937-a05f-370c14db6e7f | -23.76915 | -50.74484 | 2025-10-25 04:23:00 | NOAA-20 | SÃO JERÔNIMO DA SERRA | PARANÁ | Brasil | 4124707 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 9216a044-9a15-3af0-9a5c-54949541ca93 | -23.75789 | -47.51181 | 2025-10-25 04:23:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 89e386f8-087c-3e2b-a8a0-5a09796dabf3 | -25.14361 | -49.14886 | 2025-10-25 04:23:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fabdbbdb-49bd-329b-9324-7ffbf2591d18 | -22.18196 | -44.13152 | 2025-10-25 04:23:00 | NOAA-20 | SANTA RITA DE JACUTINGA | MINAS GERAIS | Brasil | 3159308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 623682bd-024f-3b84-b711-a3df506c023d | -22.83483 | -51.35886 | 2025-10-25 04:23:00 | NOAA-20 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| d67592d5-87ac-35da-98a0-8e6af6612975 | -24.13086 | -49.69585 | 2025-10-25 04:23:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4cda79d8-335b-31b5-a4a8-aeb312c1a2b0 | -22.28673 | -46.82798 | 2025-10-25 04:23:00 | NOAA-20 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 18a7985d-e4dd-3b2b-8b0c-f1c2e0778e45 | -21.88668 | -45.27133 | 2025-10-25 04:23:00 | NOAA-20 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 10f7abb9-13ec-3c9e-956c-b41866667116 | -27.18685 | -51.42751 | 2025-10-25 04:25:00 | NOAA-20 | HERVAL D'OESTE | SANTA CATARINA | Brasil | 4206702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a2a6a907-1d47-32e3-b462-7165e3d7bb0f | -28.736 | -49.11861 | 2025-10-25 04:25:00 | NOAA-20 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6673bb16-1b5a-3086-9c56-835aec2e4638 | -27.54737 | -52.96346 | 2025-10-25 04:25:00 | NOAA-20 | TRINDADE DO SUL | RIO GRANDE DO SUL | Brasil | 4321956 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 91d2cb70-1590-309c-814c-0ce097ee4faa | -28.95723 | -49.51898 | 2025-10-25 04:25:00 | NOAA-20 | ARARANGUÁ | SANTA CATARINA | Brasil | 4201406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 917cebd3-9551-3864-a34e-214f52c04f91 | -28.83593 | -51.00557 | 2025-10-25 04:25:00 | NOAA-20 | CAXIAS DO SUL | RIO GRANDE DO SUL | Brasil | 4305108 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| d8c54b5a-d242-3af0-840f-2418c86e6e64 | -27.54381 | -52.9627 | 2025-10-25 04:25:00 | NOAA-20 | TRINDADE DO SUL | RIO GRANDE DO SUL | Brasil | 4321956 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d6e8e682-f3ce-3c0f-8d17-0da7d85fa772 | -28.73873 | -49.12323 | 2025-10-25 04:25:00 | NOAA-20 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3c0f23c4-5706-3cc1-9610-c320a90accad | -28.73659 | -49.11463 | 2025-10-25 04:25:00 | NOAA-20 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |


[Clique aqui para ver as próximas entradas](README49.md)
