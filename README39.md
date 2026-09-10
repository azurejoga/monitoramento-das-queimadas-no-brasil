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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9018e79c-fa89-34ac-998a-4eab95e75f37 | -6.95546 | -59.74882 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf60167e-fc8a-3052-9b4f-55d760e54030 | -8.9928 | -65.41832 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6b0028c-c61b-326a-b68a-824184a85685 | -6.78722 | -58.89648 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c10d18ce-ef57-322d-929a-e5ea5d0f2e90 | -6.89812 | -62.98204 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 679c4512-ff0a-39dd-904d-df6254895130 | -8.88894 | -61.42795 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bb8b193-e595-307a-bdb7-5d4e32acef6b | -4.86081 | -56.00269 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ac6b328-2d1b-39c8-b516-9e0d5003b606 | -6.05994 | -57.79184 | 2026-09-10 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b516ecd3-e3d7-3f01-99e4-8bfcc7bbce47 | -9.83635 | -59.46887 | 2026-09-10 05:48:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc29c134-c117-37bf-9855-ee18e3bab9d3 | -8.71485 | -62.44164 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2796e4dc-1504-374c-a195-c6f444f7b378 | -7.01587 | -59.77916 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7efa4443-5918-38f1-9262-5a577673b1f5 | -6.82645 | -58.99225 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3226bade-a028-325d-97a1-d7f9a6e9e134 | -6.78421 | -58.88885 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a72a297-59d7-306d-8ca1-1d5dcaaca3f4 | -9.04109 | -65.74719 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d5beabb-3d41-3e2c-9295-965b7d9efd65 | -8.73369 | -62.38711 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e07f51c2-3a37-32ba-88a8-b4138b5fd3ad | -8.90624 | -61.43474 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71752cdb-0071-30ba-aa9e-0c3daa4e3774 | -6.45713 | -60.03423 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cef1432e-8047-3465-919f-ae62a127caf0 | -6.76307 | -58.61464 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 214fbc79-b415-3a85-a9da-186b006e72d9 | -6.81211 | -60.13486 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 896e6266-c0c1-3e91-9f7a-96e5b025d24c | -6.45781 | -60.02977 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef9da23f-ade6-308e-95b8-b3e102b86318 | -6.55413 | -62.89605 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| bb7a29f3-87c0-3110-91a2-11247572da14 | -4.85848 | -56.01862 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 368b1260-8881-305c-a20f-ccedc4b223ec | -6.95329 | -59.76297 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40b7dd06-e725-3249-a605-fbd3dfec2c65 | -6.75904 | -59.74121 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5736f77c-d0bf-3baf-9778-21f0747ece90 | -6.55469 | -62.89252 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 75dd03c3-4f2e-3ac9-b12f-86d11273e4ce | -6.76361 | -58.61101 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85a4fe8f-3a08-3d74-b30a-083446f6135a | -6.76597 | -58.9576 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d85f0e0-8390-3613-9b7f-a81b910c0f3e | -6.50375 | -58.38539 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b97388cd-0124-3865-8ea9-e85efde2e37a | -6.78069 | -58.88471 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9372c6f4-161a-3a81-be85-a6955f89b97d | -9.2488 | -65.67345 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81a7eb15-8a5d-3880-a88e-9a0db9c97c8b | -8.43463 | -70.09782 | 2026-09-10 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9598bc17-8395-341c-90ed-633c64341fe6 | -6.78773 | -58.89296 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0d9094d-eb3e-3c75-9df6-5ddf38ad013f | -6.95424 | -59.74591 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69b7b6d1-13a5-32f0-8ce4-3782259b8f36 | -6.55804 | -62.89304 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f744ed1-9df2-3b07-acc3-a707bd84fca3 | -8.15242 | -62.89943 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8031e5b8-c6f6-3a90-a586-722d5829f444 | -8.68791 | -62.46025 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e770e16-85f3-319e-b196-366046791b03 | -8.88946 | -61.44895 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bcd61dc0-ea68-3e7a-9242-1ec49defcdbf | -6.46054 | -62.86708 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e06c5866-c1a2-311f-b644-b24390f50b39 | -6.79228 | -58.89003 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f601fee4-b64c-372a-8526-211eea972178 | -6.8757 | -56.51233 | 2026-09-10 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 420dcd43-60e0-396c-aabf-9c1ff0e61228 | -8.99036 | -60.58057 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d71cc8e8-6819-30f6-bcd9-fd60afbd2ee2 | -5.36929 | -56.02146 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b47aad36-084f-335b-b3f2-e751e2781a69 | -8.82266 | -62.48809 | 2026-09-10 05:48:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf2bc870-0da4-3e0a-bf34-981a67dbda0f | -6.4585 | -60.02528 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64b21049-575b-3101-a969-d49a30162325 | -9.25731 | -60.93228 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0152431b-96f5-37cf-a63b-72c7d173a9fd | -6.24916 | -51.67703 | 2026-09-10 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d192453-dfcb-3c6a-809d-9b81bc6a0a41 | -8.99616 | -65.41888 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e508eb96-6db0-3e12-b50d-342668aba010 | -6.24266 | -51.6763 | 2026-09-10 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d344ce9-1240-3ad6-9d20-c65a96f1c3cd | -9.22062 | -63.63864 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 669593fc-8827-3968-9747-019b233c95e8 | -9.04004 | -65.41103 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f52246d-548d-363b-9d2a-3fe67bfacdb1 | -9.70617 | -61.93129 | 2026-09-10 05:48:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d6cb549-a817-3085-b4e7-5a812aed405f | -6.4045 | -54.96756 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4a00460-71b4-3f4c-983d-2d2fd4db3eb9 | -6.86683 | -56.57312 | 2026-09-10 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 014816d7-d393-3f73-a9be-d6fc08415447 | -6.55748 | -62.89657 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2085baac-c119-37cf-9812-d160abb7e952 | -6.90147 | -62.98256 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e1da8673-6772-3380-be35-d3b010be617f | -6.76822 | -59.43215 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d4461e88-441f-3628-85c5-a92ea7a4b80d | -6.54912 | -62.90611 | 2026-09-10 05:48:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b353b1b-09e2-3452-9b80-bf1058c9cb64 | -9.13677 | -64.40906 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e219b79b-a1d1-3d96-aa25-abd136a3650a | -9.21841 | -63.65278 | 2026-09-10 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e01e52d-ca02-333b-bc41-7bfea620950f | -8.62961 | -66.51031 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd379650-5dc5-3206-825a-e427c9d2e61c | -8.08408 | -54.85357 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| cd0d256f-5b1d-3e28-9343-f9f2ac75207a | -9.13345 | -64.40852 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| feaf41f5-049b-34de-bc6b-605afe82227f | -8.68734 | -62.46398 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a7828b04-ff5f-36e4-b382-0495cee01797 | -6.82723 | -58.98705 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d8a319b-cb18-3423-8d5c-43ee5296c6b4 | -6.77916 | -58.89523 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8eeff4b7-0a04-36e7-84ca-9dc92397cb9b | -6.81277 | -60.13042 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c5f439e-b7ae-38be-8141-311bb0ae5773 | -6.79563 | -58.95119 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cd22ebb-a0df-3541-bed2-2842028195f4 | -6.50489 | -58.37786 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e66a13a7-34ad-31f8-ba06-7558d97b80e0 | -8.15298 | -62.89584 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42f1dc34-09d7-3006-bbf2-dc0c3af26650 | -6.45338 | -60.0337 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3e2d3da1-7607-386a-afb3-110baa853969 | -8.99104 | -60.57606 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5e0ce8ab-9779-300f-92cd-234c66fbd482 | -8.9907 | -60.58379 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b7fb866-4137-3e30-ad17-01e3a3dd7e7c | -7.24649 | -59.51868 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81fc53de-385b-3323-929e-57e1adb8b9e2 | -8.73177 | -69.49317 | 2026-09-10 05:48:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bcc0bec-52b3-3aa4-99c9-91824daf10fc | -9.0037 | -65.40143 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cb46b09f-20ac-310c-bb87-2aa1bfa5ba69 | -8.67821 | -62.45494 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16b0e3e6-5f0b-3168-b1e2-ced16b31ceff | -6.6816 | -59.92603 | 2026-09-10 05:48:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5eeddd35-53cd-3746-baf6-5885f32177e2 | -9.67847 | -63.43329 | 2026-09-10 05:48:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1c03d0b3-3204-3444-9dfa-a7dfea076312 | -8.9233 | -66.85293 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e5ad4f3-8356-3f8e-adab-50f980145261 | -8.9793 | -60.60966 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6555fd3-c2e4-30c8-abcb-ee88549a8e4b | -9.20478 | -65.77393 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ff687dc-2d73-3bb4-a770-9313a470222f | -9.08228 | -67.8695 | 2026-09-10 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5742de5-fced-3091-a1a1-18d87488d5fb | -4.8592 | -56.01376 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1ad64ad3-5f87-3119-8089-24ec497d6c1d | -6.95402 | -59.75826 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1040b005-17e3-37f9-8763-02420498b35a | -8.09199 | -54.8509 | 2026-09-10 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fde1303a-2356-378f-91d9-810ce13e985f | -8.89785 | -61.44186 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39153671-74b8-32d6-bf46-9e025cde704e | -6.2676 | -53.11451 | 2026-09-10 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2dd23da6-ce49-3798-a344-e08e75a4c090 | -6.83123 | -58.98767 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f915b78-376b-384f-b8f6-b365dc1d57ac | -6.43096 | -62.85882 | 2026-09-10 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d338786-80a7-3a63-a5f3-74227a9d775c | -6.80903 | -60.12986 | 2026-09-10 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df0e5572-8fe9-3e19-801c-8da21e512017 | -8.68106 | -62.4592 | 2026-09-10 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44169147-d302-3f24-a830-ec96c139ff4c | -5.2753 | -55.96264 | 2026-09-10 05:48:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f060f3c-b707-39e2-90de-b0d518154979 | -8.98369 | -60.60573 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f899b992-9a7b-3cd9-84d5-970e0ec0ce58 | -6.79478 | -58.90112 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 21b08f44-4bfe-3296-a653-53a2ed0f3f03 | -6.76771 | -58.61164 | 2026-09-10 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5e94c13-e8e2-370b-bbab-bc3bd6988cbe | -8.92681 | -66.85352 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5302c74-09da-3724-9314-185bacf28294 | -6.78018 | -58.88824 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6ac1002a-4efc-39a9-982e-c02301cef220 | -6.63969 | -59.43998 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c343e71-b1d1-3ec3-8547-b2d536ab044c | -9.24938 | -65.66984 | 2026-09-10 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14b1eced-16fa-3b7f-a7f9-cbcd0972aa47 | -7.0197 | -59.77974 | 2026-09-10 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 538e2441-c5f7-3ddc-a096-ae5be2e28c0f | -8.89426 | -61.44131 | 2026-09-10 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README40.md)
