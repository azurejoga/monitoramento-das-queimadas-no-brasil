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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d79465a-1015-3005-aa3d-fc2219f2553f | -5.45917 | -60.15512 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 17be1737-1fdd-37de-baae-4fcab687ecad | -6.62101 | -53.32236 | 2025-08-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 3d4c8ede-d8a4-38ae-b1bd-0dd006b42c63 | -13.07349 | -46.33949 | 2025-08-27 01:09:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 3168a071-eae0-3ff1-81e2-4c76a8f9bcdf | -6.24425 | -60.01943 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| c776e1dd-60f3-38cc-91f4-fae7a43e612f | -9.79204 | -49.89437 | 2025-08-27 01:09:00 | TERRA_M-M | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| a2eb77cb-9b49-3632-96a0-cdfd64b0d625 | -8.87807 | -60.76608 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7326226b-b206-3d05-9198-c9deac739db3 | -13.40023 | -46.90011 | 2025-08-27 01:09:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 7ccefb4e-9d41-3ddf-99e7-0ec5232e43d0 | -5.31111 | -60.20835 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b5bee0fb-6344-3981-8b31-5ee0df008b49 | -6.9442 | -59.56317 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 45f4ff8b-521c-34c0-8736-9b7d5ff12ea9 | -6.81931 | -58.97339 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| d5a09134-2cc7-3360-a97c-c8bbdb8cc782 | -9.40792 | -62.48833 | 2025-08-27 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 1b9cc38b-d1d8-365e-8614-45caf7425576 | -8.11172 | -61.47893 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 83f3878e-de63-38a7-8488-8272145f7087 | -8.12984 | -55.55109 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a5f7fcb4-cc60-3dfa-a376-65b36db80754 | -8.961 | -65.97552 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 257.8 |
| 573c82fb-b7b0-3e6e-8eab-ff744c8a4f64 | -7.47498 | -61.35401 | 2025-08-27 01:09:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 52d22564-c90e-3a0c-880b-d437b64e7229 | -11.3765 | -55.36574 | 2025-08-27 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 22c2a587-ce6c-36a8-9cac-b2223eded0c4 | -9.40636 | -60.51202 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| 82bb9b40-a908-3bfe-a7d8-829d3e1f2c84 | -10.41248 | -57.70429 | 2025-08-27 01:09:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 38162932-a632-32e5-8d82-9be56cab7a20 | -9.56204 | -55.3743 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 88357c14-7528-3138-852c-4c42befaef15 | -9.40086 | -60.5493 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f5650739-9665-33fa-88bf-2103dedca178 | -6.69754 | -58.55756 | 2025-08-27 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7b2ccd69-c5a9-3810-877c-9478d21cc384 | -9.80451 | -64.2489 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 97972024-3e38-3c06-8a60-744292e9ddda | -14.30629 | -60.36367 | 2025-08-27 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| e41cc956-597c-35ef-93be-8611732976fc | -6.62371 | -58.54957 | 2025-08-27 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c9945c0b-c7e2-3364-a146-63fcbd88c689 | -8.85302 | -62.44616 | 2025-08-27 01:09:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 15.8 |
| c9f747c8-f9fe-3712-9c74-5501945d06e4 | -8.34259 | -62.93845 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 30.8 |
| 50341400-c238-3b3d-ab94-230bdd32047a | -13.0085 | -56.89533 | 2025-08-27 01:09:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 70f34d2d-310e-32ad-a986-e53bb3938ced | -6.63386 | -53.33446 | 2025-08-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 0b1bc7e3-eb5c-35e6-acff-307b880cbfbd | -6.91777 | -52.84897 | 2025-08-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 09b7fc9e-4b9e-3a51-9c0a-a5520891ba4e | -7.05533 | -59.82254 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| dccb0fc4-8d53-3fde-af85-03503588af15 | -6.35994 | -55.805 | 2025-08-27 01:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 075ad3f5-50fd-3976-ab45-b4847dbc978b | -8.9417 | -65.9466 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 333.7 |
| cf673676-6b00-385e-8df9-a01fe59b6a2b | -11.82292 | -46.81056 | 2025-08-27 01:09:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| a88c4c57-f987-3726-a5f1-b54a7192fafa | -7.43663 | -57.62846 | 2025-08-27 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5ec022dd-8968-3741-bb47-c4c0b4c36fef | -9.09757 | -49.57861 | 2025-08-27 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 304.8 |
| 752c4c70-c399-3c0b-aaba-56288763d1a7 | -8.94548 | -65.97749 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.6 |
| b6716717-a82a-3ab4-bc03-4c4f96800b01 | -9.10147 | -49.60261 | 2025-08-27 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 4c812b91-8286-30d7-af04-64cc159942ff | -8.90017 | -60.77557 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9bea8d9e-0a62-39e8-b535-b40b57da7324 | -6.7182 | -58.56677 | 2025-08-27 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f0d91d2b-2ae9-3402-8b1b-0bd8388b529f | -9.28823 | -63.71924 | 2025-08-27 01:09:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 2cec459e-da10-3164-a5fc-efe7cc89c7d3 | -6.25368 | -60.01813 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.0 |
| ec569537-318f-3149-848d-d1b9a71d46f7 | -9.06524 | -66.0828 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 9de34285-6c4b-3411-8ee6-a3636f1a97a6 | -8.91262 | -60.71198 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 938eec42-8c3c-3072-8bb0-87fa972455d4 | -9.17738 | -59.46988 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 359a2acb-ff73-363a-9a8a-9d33dc681899 | -7.27779 | -46.9936 | 2025-08-27 01:09:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| fc36d222-9ce0-3e54-8618-242d13ff0277 | -11.36882 | -55.3764 | 2025-08-27 01:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 487e53d2-7f43-3c8a-a934-2c102c350a1b | -14.53403 | -53.20337 | 2025-08-27 01:09:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| f11a77e1-3940-3fe1-be2a-0ec6989d5dd1 | -6.79829 | -59.63584 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e4b16c6e-e324-3a4b-b90f-e572129576dd | -7.03925 | -59.8454 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5cfb7f7f-832f-3cb2-952a-745d38cb65b1 | -9.0936 | -49.55421 | 2025-08-27 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 87aa11da-befe-3d5f-8247-7d8358fa7722 | -8.93754 | -65.93992 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 241.3 |
| 86f7717c-fd91-3769-a0c2-6a0f0addf9e6 | -10.03467 | -59.36601 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dacbc0a0-d0d2-36cc-890f-31132010cad6 | -6.76631 | -59.6804 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e3b5d180-1b67-3852-ac04-0e23f11e72e8 | -8.71593 | -64.03091 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c52d8c37-0384-300d-b348-b8d2bc94e65e | -9.27223 | -56.9116 | 2025-08-27 01:09:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| be3c202d-892b-3ea7-be5d-b7e4f933a45d | -9.08362 | -49.58084 | 2025-08-27 01:09:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 53845327-ef7b-3f5d-90ad-0a085ad10bb0 | -9.16117 | -59.56688 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 60a9c7cb-f5e7-3afb-8303-4077acac28ff | -7.44185 | -60.02884 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 729dc518-8a2c-38ba-b70b-5860e7c6adc3 | -9.41964 | -60.5346 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 2d7f1097-39fd-3567-a961-0458fa1586f8 | -9.58117 | -55.38474 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 573dcb3d-a358-3a8b-b8dd-7d661a1f930f | -6.63262 | -58.54829 | 2025-08-27 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0913a043-6153-3502-be1d-26ebcfefa6a1 | -8.95303 | -65.93801 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 220.4 |
| 2e5f209a-5930-3a7d-a8de-71edeb10f404 | -14.30474 | -60.35066 | 2025-08-27 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 25feb4f2-d415-37e3-9b37-632b53fd0b17 | -5.22899 | -60.00167 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f7325361-ba41-3b93-bbfd-e5dfb047ba0f | -6.69629 | -58.54851 | 2025-08-27 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 07a34f8a-dbe0-381b-86fa-c860b94c74e8 | -9.41103 | -60.54791 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 3ea19a99-e04d-3b15-b2b9-a63387a93ab7 | -9.40948 | -60.53596 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 11a79695-59ef-3bbf-a669-2c9cc177f933 | -9.5903 | -55.38338 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| be297afc-6bf3-3b76-bd0a-04f856aaaa05 | -9.42121 | -60.54658 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 4ebb94db-f5a3-30f8-8129-8318cafdbf3f | -8.53517 | -62.67109 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9f209c69-5c72-359d-a4bf-fa8a2f6b5c77 | -6.765 | -59.67053 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 8d3770ef-9af5-32f7-9060-11fff23083e0 | -10.0991 | -62.89024 | 2025-08-27 01:09:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 25.6 |
| f8c84376-bf6d-3066-9084-7b43fb4005b8 | -7.25752 | -57.66609 | 2025-08-27 01:09:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| d35e3691-3e1e-37cc-b02b-3cfae7420436 | -5.80296 | -59.21974 | 2025-08-27 01:09:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af1b5718-27ff-3d13-b2e5-ef05e74abf30 | -6.62307 | -53.33607 | 2025-08-27 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 957cbf9c-8d83-3e7b-8e69-4caf282b5d43 | -8.13214 | -55.37179 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b8a363df-2847-34bf-a535-203e4a4b518c | -8.92623 | -65.94865 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 124.8 |
| b58d376b-1007-379d-aa49-e5e2663ab134 | -14.7618 | -59.73233 | 2025-08-27 01:09:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e9c4c0d0-3aaf-30b9-a944-bfd0546352c4 | -6.78898 | -59.63708 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 278f5e41-cc7c-3689-ad8a-25e39be96ea4 | -9.41807 | -60.52263 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 06e1683b-5756-3a69-90de-5fb1ad407180 | -6.77433 | -59.66931 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 38560c9e-7c5b-33c9-a088-9864ca85f6fb | -4.44598 | -56.09158 | 2025-08-27 01:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 582b20ee-384b-38a0-906c-bf649c8fff8d | -9.15983 | -59.55659 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b9e764a7-acb1-32ba-8f5d-3e8e562dc5f3 | -8.10768 | -61.48504 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ad1dc109-76d1-38b4-a692-4934a2ad95bb | -6.57365 | -47.37012 | 2025-08-27 01:09:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 4965fcba-a7ce-3984-9628-8f81dbd775f3 | -6.9504 | -60.08366 | 2025-08-27 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 99922dd7-3376-3b67-a332-cbb64cffc2cd | -10.03332 | -59.35558 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 374eea08-6d00-318b-a855-5eea7ee3fd55 | -8.53827 | -62.66036 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d8a521df-3b09-3c88-aa8b-69b4f01e9ae2 | -4.96018 | -55.81944 | 2025-08-27 01:09:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 1fa73cb0-ec2a-327e-bc59-156ca69e1465 | -7.27829 | -46.9883 | 2025-08-27 01:09:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 7abb7517-91f8-3652-a8da-144a4ee4d7b5 | -5.60963 | -60.23242 | 2025-08-27 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 91134a5f-6a1f-3d86-8a38-46e2e552a06a | -9.34438 | -59.63673 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f17bbc32-732e-3bee-9365-158893e9f647 | -9.81153 | -64.25456 | 2025-08-27 01:09:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| ae1179a8-5b52-371f-a1b3-10dcd203e7d3 | -8.89857 | -60.76333 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| cd3edd26-368f-336c-ad56-48ba7471f075 | -9.39777 | -60.52536 | 2025-08-27 01:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 879cf244-0d83-309d-9b24-fc24f32bfb8f | -9.07904 | -65.72739 | 2025-08-27 01:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.1 |
| f94a7d8b-0ca0-3c2e-bff5-687874409d9f | -9.15711 | -59.53584 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 27a8b1d8-5ad9-3d57-83d7-e3a5c69f1381 | -9.1544 | -59.58925 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 4a7f2190-3ce5-3005-bd40-e3f9db830e07 | -6.68613 | -58.54074 | 2025-08-27 01:09:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9f035a4c-d5bd-3e1c-acc5-2c2d15819d9d | -9.18855 | -60.79424 | 2025-08-27 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |


[Clique aqui para ver as próximas entradas](README10.md)
