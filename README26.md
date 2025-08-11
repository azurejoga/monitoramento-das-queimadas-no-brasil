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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0110315-27b3-30cc-88db-eccbd24287bb | -7.07467 | -59.18301 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2bb9ebb-15c3-37f6-8e9b-58b49575f114 | -7.06502 | -59.18842 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14a7b760-5c2d-3b73-84c2-8f213997f8ab | -7.08746 | -59.18722 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63935002-2ca6-3766-b4fa-aedb5438ac70 | -7.06405 | -59.19447 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 024a056b-dc44-37cf-9f23-aa7480b7bf11 | -7.01843 | -55.41669 | 2025-08-11 05:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6b09e45-9a82-36ae-959b-28f78031fe00 | -7.06968 | -59.18661 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16c1aca6-4bae-3057-9e20-917d351c118b | -9.37563 | -61.54051 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2c90c88-81b8-3df6-9b86-cdeb072ab0ef | -7.06031 | -59.18966 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d378e140-46d9-357e-8e01-4e2d1176b5dc | -7.06222 | -59.20689 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e650732-3662-3c98-90c7-eafaa9317b44 | -7.07095 | -59.20802 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5652277a-b6e8-358e-b22a-830547b84a5f | -6.09345 | -59.92849 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f893c4ff-47d5-3e84-a182-0fb0283b7831 | -8.55898 | -54.6797 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adb3be16-a5ab-3e78-803d-cbd8130e4bba | -6.10554 | -59.92218 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30f6d98a-fadc-3881-8d82-4555b9cf07bd | -7.05658 | -59.18474 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5185938a-904d-3936-b7fb-afbf83bf9a2b | -7.06285 | -59.17251 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8be30ea-68cb-37c8-ba4e-7a174294bd08 | -8.93893 | -60.73152 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02525644-a7ff-31f7-b4f2-6a1268ee52e2 | -11.12099 | -54.65287 | 2025-08-11 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 530714e5-793a-3833-826c-3f705782708a | -7.08487 | -59.17406 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 313c1f52-e2d2-39a6-bc3a-6c58889ffe08 | -11.12041 | -54.65769 | 2025-08-11 05:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55f7f92a-3b3d-31a2-850e-9e4813307b15 | -7.06468 | -59.19027 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2193f04-359e-30c4-8de1-9f394b258a24 | -7.06065 | -59.18782 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc3eb135-6531-30fb-9d05-b3280d4386c6 | -7.07733 | -59.16426 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e511ac4-d4b5-30f5-bd43-954e65ea82d6 | -7.07718 | -59.16616 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd1f7059-7b66-321d-ac17-3ed0162dcb15 | -6.93029 | -60.06418 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30fd18ce-de9f-352b-93af-4ed9315e3ef2 | -7.05785 | -59.17611 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a489aa1-f76a-3a42-8f41-f02bcb9d9500 | -7.0688 | -59.19324 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 346c5775-12ff-36da-8a3b-c8c493b95bb4 | -7.05286 | -59.17976 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0f7d7a9d-1224-37e0-9aa7-cf2100b0cc5e | -9.37247 | -61.53507 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79615c29-b000-37f9-be49-b967eb2828ac | -8.93132 | -60.75573 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75a5e453-4189-36ca-8d01-9ade54105f4d | -7.07281 | -59.16546 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c2c9230-fd5b-3254-a760-cb6421add12d | -8.93386 | -60.73806 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7cbee92-3c6b-3a61-98e3-1ab50c8f2e02 | -8.93791 | -60.73864 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6797bc5-35df-3c35-9e34-8cfa05bba515 | -7.07872 | -59.18605 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cae2687c-d7c4-318c-b18e-4ddab63a3364 | -7.05969 | -59.19384 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddbf63b4-50f8-364d-83df-925a5acb03a4 | -8.5699 | -54.69053 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a491de4-54c7-309b-97e2-03dc88365678 | -7.2543 | -59.9975 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b83504d-5ac3-3c59-95be-ccfeb7589b79 | -7.07404 | -59.18723 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93f7f089-f6c3-365e-b89e-33c94ea67f4e | -7.07636 | -59.20272 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3e855f4-c10b-3df0-bf76-fb7997b25ec0 | -7.06006 | -59.19202 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7689b05d-6ea7-37f2-9b9d-805182d61601 | -9.37634 | -61.53565 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f27d5e8e-c69d-3bc5-aca1-fe50aadc28b2 | -9.37775 | -61.52596 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 579252ae-2d45-32c0-b79b-f1ced60fd860 | -7.07279 | -59.19563 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a14bf1a6-5028-30f0-a5fb-a722c62faae7 | -7.09183 | -59.18786 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 033e2d5b-22fc-3fd7-8c66-86b44855cc37 | -7.06588 | -59.21398 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 39567a05-8bd8-3d90-9a7f-6bef98e56418 | -7.05534 | -59.19318 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7de82c78-70a8-368d-8ebf-84dce4080088 | -7.07317 | -59.19382 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed60a035-e50e-3b10-9658-f63a6ba21d33 | -7.06908 | -59.16053 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9dd2171-adc6-36c2-98ad-f0ed75a9aa67 | -6.10217 | -59.92619 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 596a766d-803d-3bbd-9e66-7368909e17e2 | -7.06721 | -59.1732 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ae5b0f1-dc69-3b6e-b36d-c42684eeb427 | -7.06762 | -59.20156 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 39ed830d-6bd2-3313-b6ae-0098f643634e | -7.06594 | -59.18174 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57246472-4c5b-382d-b312-d3398a1bded2 | -7.08309 | -59.18664 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b70e0b3-f862-35d0-8b21-14c25ce8fc26 | -8.56815 | -54.70419 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be3cc0b5-5aa8-3b8a-b2fa-555d45437423 | -7.06443 | -59.19265 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ed04d7-9577-3619-af06-332eb7ba1d2d | -7.06842 | -59.19506 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4148f7bf-d579-392d-9cf0-08672073a8aa | -7.06161 | -59.21099 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ddcbfd1-cce1-34c7-b5c3-036b45d03de4 | -8.92678 | -60.75866 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4924c2ad-f527-3f87-a334-9da5feecb59d | -7.07156 | -59.2039 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1d70fcd8-4c95-3c83-b2a5-8140c2de7f26 | -9.37846 | -61.52111 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c72eb927-136e-3953-a36e-9a9d1d0a9904 | -7.08628 | -59.19558 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7766491b-6547-329b-abff-88bb1a029529 | -8.57595 | -54.69128 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cb17a57b-3203-3618-8f3f-84c9903f6cdf | -5.3413 | -55.90511 | 2025-08-11 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26646966-5179-3033-9c19-3e8835c8eeab | -7.07297 | -59.16357 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8035c896-c520-383f-81b1-d6dd0058945a | -7.07793 | -59.16 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 214be303-2311-399f-9f6e-576727390e6e | -7.06344 | -59.19862 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e59e8aa1-4205-3a5a-9259-1aff77baedd4 | -8.92679 | -60.72979 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3273ec13-3d4f-31fe-9227-089e868f95e3 | -8.56385 | -54.68973 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b93431f-51d7-3050-81d2-82d846c690db | -8.56269 | -54.69879 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8913fe15-2c85-3c30-a7f4-a50742dc958a | -9.38162 | -61.52654 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 872e0f3f-d0ed-376f-a765-864e814acb6f | -7.07344 | -59.16124 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7ac2815-95da-3dc7-bfe6-94e9566d6dbc | -7.06999 | -59.18474 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d158f34-9c1e-398d-b7cd-129d497469ba | -7.05786 | -59.20622 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3241db7-6d75-3c3c-acb3-dbe8f5c47bd1 | -8.57537 | -54.69581 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8647c136-1c67-3afe-9d25-812add26b35a | -7.07356 | -59.15931 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18f9ef25-8b96-389a-82b6-50c7cb705397 | -7.06781 | -59.1992 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2a0a3d29-ba27-3539-9a6d-f2ff7acd8dbb | -7.06267 | -59.20513 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5a06df57-464b-332d-9401-3f3b447070cd | -5.3462 | -55.90887 | 2025-08-11 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 191907ec-ef61-3c03-bdac-67e0633fa46d | -7.06682 | -59.17556 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3495af00-3d0c-3015-a0fe-a8e5739453de | -7.06562 | -59.18414 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1ad3438-9c0a-34f4-8de7-9d19469c785a | -6.10271 | -59.92259 | 2025-08-11 05:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcfb6d0f-01e8-3fe6-b63b-00e8c923bde2 | -7.05098 | -59.1925 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05c52b6a-fa5c-3859-a650-d1f1d5160ead | -7.08014 | -59.2075 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c28e2842-eab4-3bea-85e7-8a04669a9ccb | -7.07695 | -59.19855 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4efda33c-06f5-3285-b026-6770c4501203 | -8.56444 | -54.68512 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 425070fc-1033-3007-bbfa-d8130a027a4d | -7.07178 | -59.172 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcc73070-38e9-3dc3-b2b4-5e98118db66d | -7.07218 | -59.19977 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9df1d5c8-b1fa-3e9b-9bd4-d6797320539c | -7.07093 | -59.17815 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4489b887-da73-3d02-b93a-04bca88429df | -7.01789 | -55.42063 | 2025-08-11 05:44:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bed903eb-4423-32d7-a8c1-39d4dba88727 | -7.06658 | -59.20746 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e996eb94-3b5d-3b4d-bc8d-88e50712c7d6 | -9.37318 | -61.53022 | 2025-08-11 05:44:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72d695eb-70c3-3da4-aa81-1bb1ba4ff917 | -7.0686 | -59.16285 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02715ce2-fb3c-3eaf-ac5a-927b81aa42e6 | -7.08073 | -59.20332 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b12b9ef7-c63b-3959-8dae-cefab92e004a | -7.06801 | -59.16707 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebb5b3c6-b357-3f91-9ec8-0f78d08922fb | -7.06905 | -59.19084 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 646f57f4-9a99-3e10-a545-7a71430f0db3 | -8.94087 | -62.22094 | 2025-08-11 05:44:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 089ef17b-2945-38d7-a181-7764d3fb2e72 | -7.05722 | -59.18043 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23344c89-8449-3b83-874f-b9d52876299d | -8.56931 | -54.69515 | 2025-08-11 05:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bb0907ea-dc14-330e-83e0-40ae07f4c280 | -7.06384 | -59.19684 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8a28c61-bac4-3c0c-952d-bae896677ac1 | -7.08191 | -59.19498 | 2025-08-11 05:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c5cd906-e4b4-3a7a-8707-9b37dacc1d8c | -8.99167 | -68.45882 | 2025-08-11 05:44:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README27.md)
