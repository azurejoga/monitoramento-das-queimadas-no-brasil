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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dfe120a-618d-39d7-8c7c-06dce75873b3 | -19.84734 | -46.45078 | 2025-09-16 04:04:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4a32dcc3-1c91-311d-8fb4-983241f80bd0 | -17.12171 | -41.25868 | 2025-09-16 04:04:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f74337d-6557-3051-9380-3bb418e9c255 | -14.28541 | -45.99993 | 2025-09-16 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae6940e2-2432-3bec-897f-22559a54a22c | -16.68632 | -49.76447 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4d62cae1-3357-381d-a6e6-689226650d45 | -12.98184 | -47.95451 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8c7f3b1e-93db-3830-8c4f-65874e22c340 | -12.61654 | -47.94447 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 397160a5-6b54-3749-b0be-ace331436d93 | -17.23698 | -43.42709 | 2025-09-16 04:04:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2be5aa6b-2ca3-36ac-81f2-65f29ebf5739 | -15.09503 | -52.48524 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 715a81ac-749d-3aea-a957-07ef58edaac4 | -17.86431 | -44.43965 | 2025-09-16 04:04:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebf00b48-6509-325e-928a-651d81c35609 | -14.80443 | -51.66998 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 636fca2a-e0d6-3be0-a6a7-fc6f0ac414e1 | -14.52278 | -47.34467 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| defccab3-96aa-304e-b6fc-315f20f46b57 | -12.79509 | -47.18973 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be6d829f-bb93-3745-ba37-a5393d3b2ea6 | -13.02569 | -47.96617 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2101f8a-8d64-3bdf-adac-8d32d047bb31 | -15.40489 | -41.70935 | 2025-09-16 04:04:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| deafffcc-6479-3539-b677-6381cff54d92 | -13.28542 | -54.24288 | 2025-09-16 04:04:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 35c259cf-7bc4-3858-abc4-c2aa591a804e | -12.80869 | -47.2436 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef578680-7c65-3389-b5ba-04dd1b07f688 | -19.87963 | -44.90627 | 2025-09-16 04:04:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9fb284cd-4dc4-3321-be68-b716a724fa6d | -14.51796 | -47.3924 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1a163e2-6154-34be-883f-aa0824a72847 | -17.12506 | -41.25928 | 2025-09-16 04:04:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 5db6c178-f45b-3078-82b9-68c3f9a33876 | -12.80309 | -47.25069 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b93cc0a-0ef5-3a88-866f-b06272b14857 | -12.62346 | -45.75241 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 650dcd73-f0e3-347f-9126-920a989591b8 | -12.63302 | -47.51765 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a95ed31-d7e2-3d0e-b603-f6513bad5872 | -12.70112 | -47.74781 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d232c06e-07bb-3eca-a0bf-8f00bc666ea6 | -14.58525 | -43.89078 | 2025-09-16 04:04:00 | NOAA-21 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaedd72a-b1d0-33f7-8b07-fa6f245f4d25 | -12.73764 | -47.19933 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| deb75d2b-2799-3a73-9320-4980c2b3c094 | -12.69482 | -47.98901 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 48af4e29-3992-37a5-a616-7925bb6ca326 | -15.82193 | -53.47551 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8ee7876-1701-35c4-a27f-04ce050ed95a | -14.92318 | -51.64792 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9171e8d-6191-38c0-ba6f-8e90fbf30b71 | -12.95329 | -47.96331 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5a7eab46-f2d7-38d5-b6e2-faeb0bc83391 | -12.62229 | -45.75456 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 898ca1ee-3e3e-3ed7-a26c-e125cef3fec1 | -13.7394 | -48.76595 | 2025-09-16 04:04:00 | NOAA-21 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4160c1ea-0db0-3a50-bf57-cd3836c4acca | -15.843 | -53.47377 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 020e9b82-c91b-3a47-92e7-66ae07272a41 | -14.87063 | -51.61805 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39dc10e0-0af5-33e9-abc9-5eb467013ec5 | -12.61742 | -47.98964 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cce1bf6a-b6d4-3154-8d0c-65a7ec06b81b | -12.79539 | -47.26157 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a08970b5-37b9-3656-94a5-0da7fe68ccc3 | -16.68904 | -49.77715 | 2025-09-16 04:04:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4a4e2ad-6d45-314c-906d-c1743bda29e5 | -12.77269 | -47.95825 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0093ec0-374f-3ef6-a93a-1f3d767cce59 | -14.52113 | -47.33024 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 97c05df9-3366-360b-9884-2676564d380e | -12.76669 | -47.96878 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 170b7f54-d3ee-3440-8ea6-138cc628820c | -14.28027 | -46.1426 | 2025-09-16 04:04:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c44bdcea-05a9-3fc6-91f4-7436a1969918 | -12.66499 | -47.93006 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 734907d0-e502-36cc-9d44-584019f7bd11 | -16.51538 | -43.55053 | 2025-09-16 04:04:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ffd5a55a-d9b5-3852-9286-f1692beb6c2b | -13.00189 | -47.94899 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c21b7131-74bb-3b18-9004-ac55cdea503f | -12.83435 | -47.22043 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e1a6e4a0-16c8-3b93-b21b-718a50cbb474 | -13.88156 | -44.85058 | 2025-09-16 04:04:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0623da0-023d-3b19-9890-c43514c76849 | -18.59035 | -48.1443 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6ed7265-783a-3771-9f16-47602ac131b3 | -12.64737 | -47.99961 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| af9d7c35-1820-31b5-856b-bc080abb072d | -12.62655 | -45.77504 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6e76efda-0edd-3fc0-8ae4-4e81536d7adc | -15.61757 | -47.37027 | 2025-09-16 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7766e035-3fba-3413-9d50-7f22f029b4b4 | -16.24051 | -48.15472 | 2025-09-16 04:04:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1245b9e7-162e-3a3b-af58-a76cbd51cb14 | -17.30205 | -40.68189 | 2025-09-16 04:04:00 | NOAA-21 | UMBURATIBA | MINAS GERAIS | Brasil | 3170305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 19829296-2d95-3d63-9fec-4cda07600f39 | -14.92427 | -51.67001 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f98bc5a3-d128-3b01-b6da-d6c68d66bc06 | -12.77194 | -47.96246 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ecf846fd-05c5-334a-9920-9adc728b3b52 | -14.80371 | -51.67351 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a618164-f7a2-398a-aa7c-b9179b3796ef | -15.78053 | -53.44917 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6ebe4837-3bcb-3886-a20b-e0cb0d7f2614 | -16.78772 | -40.94318 | 2025-09-16 04:04:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d33cf02d-6755-3ec2-8890-432475b2b106 | -12.67445 | -47.92363 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3c5b847c-c865-36c6-81a2-c8a9e0711081 | -14.91712 | -51.6503 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 92959d0a-a4b0-3fe8-8e76-6a4309e87ed7 | -15.08942 | -52.48404 | 2025-09-16 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 958cdbdf-bfa8-39a8-adb3-ae36aacac255 | -13.21336 | -47.28764 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 44a7134c-0dfc-33b8-bc84-a18d064b8ee3 | -14.53738 | -47.35537 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d29f3d55-3e81-3d7c-9818-3c9399372ce5 | -15.62155 | -47.37114 | 2025-09-16 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 2c1b0eb8-3512-31c3-a615-0bed20e37de5 | -13.19779 | -47.30305 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 35ad517f-dfec-386f-81b3-61c3a4f4a1b4 | -18.55508 | -49.26196 | 2025-09-16 04:04:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 10ac5a67-5fcc-331a-91d9-46fc512ddc12 | -18.55674 | -49.25337 | 2025-09-16 04:04:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.9 |
| e8989251-b86d-3804-b9c1-c808ab544b79 | -18.87193 | -43.3554 | 2025-09-16 04:04:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 025ee353-d75c-39d2-9576-5fb937cb9cd9 | -16.93595 | -44.06857 | 2025-09-16 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab02d509-3b05-3ee9-8d23-eb4ffe42c125 | -15.62554 | -47.37195 | 2025-09-16 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 12.5 |
| fe6ec348-aaf9-3f1b-98e4-57a4b142cd73 | -16.28779 | -45.68543 | 2025-09-16 04:04:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0764099a-4563-32cf-98a1-9d495e251331 | -13.20623 | -47.30379 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1e506afb-d7cf-3d2a-b77d-5cc48be65156 | -12.65983 | -47.92974 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0475c74a-7527-3e78-9bf7-01737a8964d1 | -12.69119 | -47.72855 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc5a530c-315b-3b8a-b84e-c87b321779ab | -15.7814 | -53.44507 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81062cb4-a109-3ace-8080-a52b028556bb | -14.52946 | -47.39875 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51fb82ef-0dcf-3fab-93f6-91ccbbe88d6a | -12.63226 | -47.51668 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1ef65c7-839a-312c-a3ad-3bc34d2c76df | -18.62176 | -43.89659 | 2025-09-16 04:04:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 177a411d-ce5d-36c6-a1de-8c9abdd169d9 | -14.9271 | -51.65602 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16afc338-b6a0-3fd3-a31e-d28d8eb203e4 | -12.29071 | -46.40404 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| f1836ae6-c205-3f15-add5-6670f6871bac | -18.39832 | -49.33702 | 2025-09-16 04:04:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24be11c0-04d7-3da2-ba00-69a1a7b7f283 | -18.08685 | -42.76695 | 2025-09-16 04:04:00 | NOAA-21 | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 363e8589-c048-32e0-8386-7f7cd320cd15 | -12.84608 | -47.13148 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0b843c3-9d33-3d9b-817f-feec4f449a53 | -13.21717 | -47.30086 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa1c779c-6532-31b6-a889-a301e8a703cf | -19.76806 | -45.85904 | 2025-09-16 04:04:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a71b0b8-13b2-38b8-948f-271dcf7b38b1 | -12.63119 | -45.77097 | 2025-09-16 04:04:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fad7aa68-c0b7-3dcc-a64f-863ef1125e29 | -12.75809 | -47.96418 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6f0d4275-f8ee-3dd7-a616-73fed524ef6b | -14.80122 | -51.6583 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 905ea7fc-1d9c-3ebd-86bf-c8cd174f39b9 | -18.39898 | -49.34116 | 2025-09-16 04:04:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fda4f86f-aaaa-3cdc-b519-77c9ad78d2ad | -18.90267 | -49.57947 | 2025-09-16 04:04:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c3f9a6af-4cd4-3b08-9a93-3aba9638b4ae | -14.52645 | -47.34608 | 2025-09-16 04:04:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 09380198-b7eb-3957-95f8-bd5350dce295 | -14.87528 | -51.62267 | 2025-09-16 04:04:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1494642b-ced5-3c37-9ab2-7acb3b01894d | -12.29743 | -46.40252 | 2025-09-16 04:04:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 74ec6537-49f6-333f-b062-eaa3f85f51c3 | -15.8413 | -53.4713 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 331e40bb-fe8d-3b25-b518-a54980eca018 | -17.94499 | -45.25137 | 2025-09-16 04:04:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a6f2338-126c-31bb-ba7b-8a95379563ec | -15.8147 | -53.46211 | 2025-09-16 04:04:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f7bdc2a-5771-3978-931a-0c8dfaea950d | -12.66702 | -47.94003 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62bbec6f-01ca-37fd-a73b-04eee5dc7f7b | -13.20547 | -47.30811 | 2025-09-16 04:04:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| dee31541-9045-34e0-bb4d-b37ade013d3e | -16.69407 | -46.94287 | 2025-09-16 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b95b778d-2a3c-3970-bd80-926cc7039cbe | -15.89575 | -47.31287 | 2025-09-16 04:04:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bbdacda-170c-35c1-909f-bd26a2fca891 | -12.77183 | -47.9654 | 2025-09-16 04:04:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 479970eb-c3b4-3256-9535-90319d6ee6be | -14.6104 | -46.38881 | 2025-09-16 04:04:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README28.md)
