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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51ccb69a-171f-3110-9a2f-61f2e0a23364 | -11.40541 | -46.32957 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fecd7472-31a9-3d1e-98f9-9c364c6b6983 | -14.44984 | -45.6911 | 2026-08-15 03:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11bc1fa5-f761-3501-b54b-7fff256d5384 | -14.4447 | -51.92192 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 125fa17e-b818-3974-934b-9c6d54ff67b9 | -14.45191 | -51.92375 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c5c6e3e1-bdc5-38ff-8832-af5c7843454e | -13.69166 | -46.26325 | 2026-08-15 03:55:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5575a2a-7003-3e6d-91cc-dd376d22e2d5 | -14.74925 | -48.24714 | 2026-08-15 03:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e088443-7fb1-3435-b88d-bc5b8502697b | -10.4173 | -47.98288 | 2026-08-15 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d248c5b3-1200-3dd1-b99d-7171d30b8ee0 | -11.40617 | -46.32988 | 2026-08-15 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c9fac13-fb08-33a7-9ddb-adb0e9c516df | -14.95466 | -46.62716 | 2026-08-15 03:55:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7cdff52-5487-35df-91c4-d16fdeea41c1 | -14.4536 | -51.91616 | 2026-08-15 03:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bd4233c1-1c9b-3e6b-b1ca-fbfdcb22ccf5 | -20.80444 | -44.73765 | 2026-08-15 03:57:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0a4eaf6e-3eec-3487-aa87-25ba234ad049 | -20.28731 | -41.62078 | 2026-08-15 03:57:00 | NPP-375D | IRUPI | ESPÍRITO SANTO | Brasil | 3202652 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 46a1346d-ba5b-328c-b8f7-db95bca2bae5 | -18.7208 | -43.00935 | 2026-08-15 03:57:00 | NPP-375D | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fae1c306-52d4-36bc-8629-0b28c00c8948 | -22.67723 | -47.55408 | 2026-08-15 03:57:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| cb174d98-cf62-3fc2-a3bf-dc8e63d2fcfb | -21.46716 | -48.61403 | 2026-08-15 03:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 267b8d5c-d8ec-3388-838d-a202cbdde3fa | -20.45948 | -46.47426 | 2026-08-15 03:57:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e99729b-84d1-3d13-b486-0aaddf1998cc | -22.33758 | -48.49327 | 2026-08-15 03:57:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d3a0e06b-d8b7-3527-aa1d-66d7b9d23a06 | -19.68327 | -42.05708 | 2026-08-15 03:57:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 545cdbd6-bd86-351c-86f6-75073375e574 | -18.57997 | -47.14747 | 2026-08-15 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac026512-f36e-3226-9bc4-cbe93e441374 | -22.34347 | -48.49108 | 2026-08-15 03:57:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ebc89f85-987c-38c6-9587-14b3ba88080f | -19.988 | -42.04629 | 2026-08-15 03:57:00 | NPP-375D | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4865d33f-2768-3c67-a4d4-31ae95ede171 | -21.11868 | -43.7902 | 2026-08-15 03:57:00 | NPP-375D | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2b3e524d-2436-3232-bc2e-64b790565ead | -21.46638 | -48.61757 | 2026-08-15 03:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b373f0aa-759b-3da9-ac4d-82a46a95492f | -19.93429 | -42.13523 | 2026-08-15 03:57:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c875fa1c-32e7-3025-b958-2c47a1ef4159 | -19.93796 | -42.13595 | 2026-08-15 03:57:00 | NPP-375D | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 01e44797-6e2d-3cb4-a602-4959710b3b50 | -20.01456 | -43.89561 | 2026-08-15 03:57:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 685ac89c-3bb2-3a2e-a373-638604707fc9 | -19.68214 | -42.05461 | 2026-08-15 03:57:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d490dae-0f2a-3934-84e1-a282dcb14cbc | -21.52203 | -45.63667 | 2026-08-15 03:57:00 | NPP-375D | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0d152977-c16b-3a0d-bcbe-7454094a0075 | -22.34276 | -48.49429 | 2026-08-15 03:57:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f9db537e-327b-3e6d-a936-7b3b278749ff | -19.25208 | -44.37369 | 2026-08-15 03:57:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ca86494-1b47-397d-b0d3-422157bc23e5 | -20.65364 | -42.49162 | 2026-08-15 03:57:00 | NPP-375D | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7678195b-3593-3a1c-a227-28633a7fccbb | -20.33265 | -46.7494 | 2026-08-15 03:57:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbd7a996-e9a2-3ce2-8afd-d67e308a8477 | -18.97048 | -43.09331 | 2026-08-15 03:57:00 | NPP-375D | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 455c8b0b-0d25-3398-90d5-a442ecafaf3b | -21.45999 | -48.67178 | 2026-08-15 03:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 880260eb-b404-369b-8dda-b47569561361 | -18.58063 | -47.14426 | 2026-08-15 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43c68e1a-202d-30f1-9002-839923029e3c | -20.93574 | -44.77739 | 2026-08-15 03:57:00 | NPP-375D | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 31387c52-19fb-3e22-a8a4-8492992613ee | -20.70122 | -42.57384 | 2026-08-15 03:57:00 | NPP-375D | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a282bd7d-e8a4-38a3-bf50-f8c186e131a8 | -19.25361 | -44.37105 | 2026-08-15 03:57:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| beee302e-a296-37b7-86a0-22491b009b06 | -20.01935 | -43.89248 | 2026-08-15 03:57:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a84c17cb-db1e-31cd-9dba-e78ada2fc5b5 | -20.01862 | -43.89631 | 2026-08-15 03:57:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 890caa4e-b9d0-3d16-8fb1-d08a7f506a46 | -23.00807 | -45.50932 | 2026-08-15 03:57:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9933026a-9d51-31f2-953c-6fa2cf3e5ee7 | -21.45923 | -48.67524 | 2026-08-15 03:57:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8679e120-e5a3-30ae-a213-93063a7bb80f | -20.00372 | -43.97404 | 2026-08-15 03:57:00 | NPP-375D | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ebdc9df0-f1d9-3f1c-988d-96129f8ac128 | -19.68406 | -42.05261 | 2026-08-15 03:57:00 | NPP-375D | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| caeb5270-6a7f-3577-8d79-3800e4f81d97 | -19.69125 | -44.92756 | 2026-08-15 03:57:00 | NPP-375D | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fe4b730-098a-3bd9-aee6-c6785df4d119 | -20.45778 | -46.47809 | 2026-08-15 03:57:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c4df6e7-abc1-3b8a-9b44-ec4dedd61dc2 | -18.5827 | -47.14525 | 2026-08-15 03:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dacb2952-b0d7-30c9-b064-50c9c8867845 | -22.68319 | -47.54983 | 2026-08-15 03:57:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| ca6ae726-f9c1-3386-9072-7ec5e3374cf2 | -19.52284 | -44.09412 | 2026-08-15 03:57:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21aa24e0-4db0-3651-a293-68f430cf914f | -19.86435 | -43.87317 | 2026-08-15 03:57:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bdc76521-6be6-34b7-8d8f-a28767da1a3b | -19.25279 | -44.37545 | 2026-08-15 03:57:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fc10e65-9030-3f4f-9605-6c08ad0b5cd9 | -18.54961 | -48.19981 | 2026-08-15 03:57:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75cfe963-75a2-3da9-80fc-cbcf8c32d60d | -20.69752 | -42.57305 | 2026-08-15 03:57:00 | NPP-375D | ARAPONGA | MINAS GERAIS | Brasil | 3103702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ff60468e-04c4-3b37-95b0-feae4bcb4b90 | -19.52437 | -44.09317 | 2026-08-15 03:57:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e75433d-5990-37e3-91d9-d5143672222b | -20.45733 | -42.01835 | 2026-08-15 03:57:00 | NPP-375D | ALTO JEQUITIBÁ | MINAS GERAIS | Brasil | 3153509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5f7eaab6-e674-3458-aada-38496cd0e51f | -22.34203 | -48.49762 | 2026-08-15 03:57:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| b002ae9a-63b3-3863-88b6-f94c98f7aa21 | -22.67843 | -47.54844 | 2026-08-15 03:57:00 | NPP-375D | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| e2b1d831-0ba3-37be-b291-c6c7e14d33c5 | -6.6194 | -59.0609 | 2026-08-15 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 9a8214bf-7581-3efd-bf85-2d8654daf7cc | -6.6013 | -59.0037 | 2026-08-15 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 9f1e2a1b-d8b9-3933-94bb-136cc6e38696 | -14.4495 | -51.9217 | 2026-08-15 04:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| e853d936-1e49-3375-b567-f3b68bbc233f | -14.4306 | -51.9029 | 2026-08-15 04:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 5c0057fe-9c24-35e6-8141-c4fc3fa66383 | -6.1222 | -44.0271 | 2026-08-15 04:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 33bcd6e8-e3d4-3985-b80a-2c4d649e5bae | -14.4499 | -51.9004 | 2026-08-15 04:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 202a477e-8bc1-324f-97b9-b6f4cc211832 | -6.9145 | -43.6351 | 2026-08-15 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 7befe035-d9da-37e7-8a2d-3d74314d723c | -14.4302 | -51.9243 | 2026-08-15 04:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.6 |
| d2fca9dd-fb45-30df-a5a6-f2c1ac2684da | -6.6194 | -59.0609 | 2026-08-15 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 73ffd519-c651-3a8d-8cf2-179e1dd3a7c6 | -14.4495 | -51.9217 | 2026-08-15 04:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 641819cb-e78e-3614-8f14-0e2065f7ef18 | -14.4306 | -51.9029 | 2026-08-15 04:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 601819a6-02c0-32a2-a89d-c25302441994 | -14.4302 | -51.9243 | 2026-08-15 04:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e454f7ed-1dde-35b8-99ba-efd7d6b9ae90 | -14.4499 | -51.9004 | 2026-08-15 04:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e917e3a8-bb9e-3ec3-87c5-9f911e70edf8 | -6.9145 | -43.6351 | 2026-08-15 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| af046fad-3df0-3d2e-bfcd-3317375b5cc2 | -6.9334 | -43.6333 | 2026-08-15 04:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 2e186bbc-f89b-3b48-848e-cf4e03508196 | -11.4187 | -46.328 | 2026-08-15 04:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 31165d1f-8acb-3dbd-bb60-10cfcf870bd4 | -6.97795 | -41.29384 | 2026-08-15 04:12:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0f74e31b-557f-3622-a575-96b281b6c1d2 | -5.54472 | -45.20158 | 2026-08-15 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1892bf6-dff3-3f2f-9abf-096083265044 | -4.52462 | -38.54947 | 2026-08-15 04:12:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b24b8143-a27b-37d7-a2cb-57880e44a7ca | -6.10204 | -44.32612 | 2026-08-15 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e82cdd13-9d82-32d9-aced-414eb5147427 | -2.7912 | -49.52427 | 2026-08-15 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 448ce496-99c3-31aa-883e-75db44def242 | -4.39358 | -42.33512 | 2026-08-15 04:12:00 | NOAA-20 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97877322-5b32-38b0-8244-5f000c6fbc9e | -6.41647 | -39.25312 | 2026-08-15 04:12:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b09fd6f7-68ce-392f-971f-4f951bb54a4d | -2.79183 | -49.5847 | 2026-08-15 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b390f49-779e-3d2c-a721-f294902e21e5 | -6.12093 | -44.02863 | 2026-08-15 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 8b3eae44-0e0d-34a7-9d9b-19d6c59d96c8 | -4.13762 | -45.73171 | 2026-08-15 04:12:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22c46132-c698-3a31-8b25-10effb4a22e2 | -2.79171 | -49.52118 | 2026-08-15 04:12:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04c82496-c7af-3a7e-a5b5-dd47b73fc3c5 | -5.11585 | -41.10328 | 2026-08-15 04:12:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 89bc33fd-be4c-334c-91ba-d26cafdcb761 | -5.21745 | -45.96109 | 2026-08-15 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c03695bd-6cf8-3177-bf17-e00829b64fde | -6.44736 | -38.79073 | 2026-08-15 04:12:00 | NOAA-20 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d12649f7-2d5b-30b4-a7c7-07663195ce13 | -4.09291 | -42.49788 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2414301c-8927-37e4-8b51-63b39734222d | -4.08842 | -42.50447 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2dcd7f47-4d49-3d38-b618-d9ccb9572e3e | -3.97251 | -49.45855 | 2026-08-15 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef73ef9d-8f04-3227-809f-8d0c228a1c93 | -6.11685 | -44.03183 | 2026-08-15 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| e3bf1058-83dc-3bdc-83f5-8f7816ed7134 | -1.57484 | -47.75525 | 2026-08-15 04:12:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b58cc23-bfa0-3c97-abf9-3a5f6150a106 | -1.96626 | -48.3734 | 2026-08-15 04:12:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0bc0685-16be-3147-8ecc-f2b7508da06c | -4.10689 | -50.99258 | 2026-08-15 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7e65653e-e984-3cf7-b1af-1ae1b07134ae | -6.83859 | -41.65933 | 2026-08-15 04:12:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| acc73c9c-051f-35a3-a6cb-1898d022109d | -4.10496 | -42.49995 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5a883fc9-61f1-386c-903c-c95cd8ccf089 | -4.10381 | -42.50708 | 2026-08-15 04:12:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 25656e12-8d33-3eb8-a232-7880f7701b6a | -6.26621 | -43.28087 | 2026-08-15 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4efd6b82-bdd8-3dd9-9e03-df9cda66c2b6 | -6.27019 | -43.27776 | 2026-08-15 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7efc5e1d-1327-3e0b-b827-12b369e43214 | -5.67065 | -43.57648 | 2026-08-15 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README12.md)
