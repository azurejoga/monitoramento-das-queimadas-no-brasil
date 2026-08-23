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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6abeaed8-140d-343e-88cd-14711cb962e0 | -7.37472 | -59.94914 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f22d3444-48d1-30a8-b7c8-0eeae636e345 | -6.20095 | -53.52917 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c4b34e3-a741-3e95-b9d1-0e6f3c7a0a0d | -9.51013 | -60.49854 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab791db6-91d7-37f2-aa9a-d5bc4ad082f3 | -6.81082 | -44.81277 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec08ead2-462d-347f-8a2b-2239ee64ae78 | -6.85377 | -59.43039 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3447899a-fb36-322f-866f-4fc97663af26 | -7.08727 | -45.00575 | 2026-08-23 05:04:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ed8f463-2e1c-36e2-b3a8-0e9352f0c441 | -11.61404 | -50.55547 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b84aecf4-e09d-3abe-8a84-89ecc5ec4e72 | -7.55186 | -61.18429 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80cbcac0-acfc-3e30-9b40-61c112f0d96a | -8.58056 | -54.78991 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95f41247-74d0-3def-a9d9-d8fe91eef3bb | -8.16342 | -52.05164 | 2026-08-23 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3207b64-d5a2-38a8-8462-1c2fb4d8b51e | -4.92644 | -56.13052 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83134bf8-2f1a-3c71-afb5-531250888ab3 | -8.51931 | -55.32547 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5b3dc0d-43a9-31b4-8540-4a232a3badc2 | -8.93296 | -48.53792 | 2026-08-23 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 759f2e59-f207-3533-b63f-8aeffe193fef | -9.50602 | -60.49783 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6df4ada1-669e-32a5-af72-1672536efe4b | -6.83889 | -59.45967 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a575f9c-3954-3bcc-9ce9-1a5604bd14ba | -9.09989 | -60.92451 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2eea19d8-38c0-3592-ad5f-99bc596d7300 | -8.52984 | -54.81031 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ab9d198-86f6-3ff1-9e57-7a89d8466a5e | -6.75693 | -58.67988 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc61229a-75c5-3087-8fc9-7c47a407f63b | -8.52766 | -54.84558 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1736477d-c6b2-3566-ab2c-844dd9efaec7 | -7.69052 | -50.74934 | 2026-08-23 05:04:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aee1b627-6887-33b9-a98f-de0a63da014a | -9.11226 | -61.59037 | 2026-08-23 05:04:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8821a652-ab40-380c-b041-0c45c5ce8b71 | -7.33828 | -55.70075 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fb8b4de-7764-36ae-be12-e03e91bb8cd5 | -9.66082 | -63.84214 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b395f770-4edf-3d81-a28e-8c6a090d002e | -6.11908 | -59.92945 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bcee949-0ffc-3823-b9f1-416817b27602 | -7.6136 | -61.60996 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 308b2e13-333e-3474-b1db-5a9422903e5d | -8.59097 | -54.74531 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cb9a87a-8e69-3965-aff1-db732c5cb89a | -8.22338 | -55.02828 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b493937-bc84-30da-af4a-6c6a854b04a7 | -7.62514 | -61.59771 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33866889-156b-3ad2-a06d-da06aaa761d6 | -9.14848 | -59.40105 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae8b29aa-4bb5-3030-96c4-e232058c9cf0 | -9.58871 | -60.50876 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b82fec8-0910-38d9-bad9-f0546b4d045e | -12.25597 | -43.18922 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 887e610c-9930-307d-b665-d8fac90775ff | -7.68294 | -63.34991 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec8a7746-f2b6-3d10-8a0e-0d02db13d997 | -6.79473 | -59.80242 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98768774-1d6c-3bcc-9d45-e92c0bf36afe | -9.06721 | -60.43337 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 304d588f-bf7a-3e13-868d-0b8b2834239f | -5.77344 | -57.57435 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 07a73f44-40d2-3f45-8a81-139fc4bc28ff | -5.78141 | -57.57131 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 67d35b91-9a43-38cc-b45f-1883d42a6f45 | -9.19239 | -59.45486 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 68a0046c-b192-3e29-a08a-1c696ca8e4f3 | -11.21283 | -55.04662 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 635986a2-d70a-3db7-97b2-dd8977ae981c | -10.33039 | -45.40578 | 2026-08-23 05:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aef0dadc-13da-3fc4-9152-1c3aa84997da | -8.17762 | -54.97462 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2bf2f6c6-e09e-3960-9f2b-b909e092f4df | -9.30619 | -56.81221 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bb0c246-bfec-3a8f-aaed-eec8684fce77 | -6.86916 | -59.03386 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e90a81d-09f0-3974-9e69-dec0e737e582 | -7.01773 | -59.56523 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c774ee2-bdb6-38a1-998e-2fc53b777219 | -9.03868 | -60.45133 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab285055-83a2-35da-9be3-382193d5c0f8 | -6.80984 | -58.64526 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a6735573-819c-3ab2-aec1-8eb54d6f3e8d | -6.81632 | -59.67182 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd47f945-72b6-37d4-ad36-98aed50db2ed | -9.79994 | -46.60681 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3baeaa62-adf7-3a36-9d4b-d805b4a28988 | -10.05402 | -46.41846 | 2026-08-23 05:04:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9edc3af-4eeb-302d-ab1d-6e5aece05a65 | -6.76075 | -58.68049 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed6e1f1e-cffd-3bad-be9d-fa3ad4292522 | -6.12803 | -57.8353 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bf5963f5-1e77-394b-b187-e4f501ad71b6 | -6.79593 | -59.79514 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be7ca4c3-f362-35f8-8264-f16323d63a9b | -11.58061 | -46.93283 | 2026-08-23 05:04:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fccc08f-8823-3faf-8bb1-7d0df579879a | -8.96077 | -50.76057 | 2026-08-23 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ded19928-de84-3d10-8d91-99b970251b41 | -6.76457 | -58.68113 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b53a1251-74b1-3f28-95f3-f52287c938e0 | -7.66909 | -61.10929 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 164966c3-6128-3d27-a3b8-fe2381e08732 | -6.97362 | -59.05919 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c23da2d4-fae4-3a3d-9fce-6c280c3c1875 | -12.24492 | -43.12324 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1d6cfc8b-2a55-3aef-8586-467003d6958a | -6.25114 | -55.42118 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0074bc72-e0d9-3d6f-95a4-46889246733a | -10.84374 | -50.97794 | 2026-08-23 05:04:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| a2c10f60-13ef-3c0e-a80c-d438c2c607d1 | -6.97113 | -59.07407 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f9002dc-ae98-3d5c-bf53-ba398499d19d | -6.79497 | -59.42699 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90cc473f-1536-3185-99c5-5fb7134dd981 | -8.35103 | -46.50574 | 2026-08-23 05:04:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1760708-ee24-3e93-b5d6-dba0f2a1c95f | -8.58718 | -54.79097 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63222daf-281a-378f-aa78-454752389fbb | -9.20779 | -59.78822 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a95c8f92-d961-38a1-90e2-89453363bf5c | -6.78684 | -58.66552 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b6041262-78c1-39d3-a0aa-9eab71adc2d8 | -4.53437 | -55.51478 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad99dc63-a901-38b4-a7e5-99cb356c3e81 | -10.45993 | -49.96713 | 2026-08-23 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aca1db99-cdba-3f91-be40-413ece80fcaa | -6.17086 | -55.56449 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26f158c8-1ac7-3e65-a44b-157bc32d5451 | -6.14025 | -59.91315 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 61a9da13-a8a8-3f4a-b397-69385041d690 | -8.80973 | -46.62368 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08bfce5c-f489-3e0d-bbca-385e0c8a4d35 | -6.72222 | -58.58904 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ec23d05-2a9e-36ce-b337-70ea41a8a14c | -6.24069 | -55.37964 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8abe456b-4cb1-37e5-ae71-ef96c0fa9408 | -6.78445 | -59.66238 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48157606-f409-30ec-8566-47cb509f8a09 | -6.13894 | -59.92078 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67b54e70-561e-3ed1-aa24-fdd21de2593a | -6.86816 | -60.01464 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 052e87b0-bb33-3f9b-9ed4-69ac1c4dc927 | -12.0726 | -50.59607 | 2026-08-23 05:04:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a3e43ff-0ca9-39c1-b8ca-a85871f84a51 | -6.96972 | -59.05852 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4d1c7a2c-7d23-3988-a141-cfc4bd9baad0 | -6.55419 | -55.09946 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae39ddb4-2234-36bd-a663-e1590f8ce2ad | -6.80748 | -58.65935 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 99f884ab-8e31-3d16-8b53-e07709976df4 | -8.5767 | -54.79286 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab83c6bc-5277-3025-a15c-6eba1b178ece | -8.52434 | -54.82368 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f7c9933-4987-3e31-b58a-5fd077e5b9c1 | -6.77836 | -59.42794 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1a09883-7ff7-33d4-9eb6-5292e73d3081 | -4.53322 | -55.52196 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2feb9cfb-e45b-3ace-9f19-916827e5e28c | -8.47403 | -46.98981 | 2026-08-23 05:04:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24900bda-1fc0-3aad-b5b2-0a330a8e61e2 | -9.40471 | -60.31461 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27ea0138-cf5e-33f5-ae3d-fb1749eb8de2 | -6.81818 | -59.66108 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56a9c4d3-4797-3654-89c4-dbdab898bdf7 | -8.16696 | -52.05216 | 2026-08-23 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5349b59-fb47-3407-b872-8b31fed4b121 | -6.75934 | -58.66572 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbe913a4-9eaf-3c7b-b246-405f68338bb5 | -6.79317 | -59.66015 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bfd5c9c-0150-3817-9cb8-534c25ef0b65 | -8.93422 | -48.529 | 2026-08-23 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1afba3e-b10f-3e46-a083-64874266352a | -8.58332 | -54.79391 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec7df39b-8320-3831-8a1e-17c396c64b0f | -6.80553 | -58.98056 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0aec2efa-8647-3f6d-907d-0219958660fb | -6.51987 | -51.44725 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0aa587a1-2ab3-32a2-ae4a-573b188650c9 | -6.79214 | -59.41941 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c1d6b5f-5ded-3d7d-ba39-b16f818d6a13 | -8.40282 | -62.68741 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9001f8fd-3728-3de2-84fa-4fd6a1df2988 | -7.61963 | -60.97775 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72eb1b64-b1f6-317d-b982-970a80e67bd4 | -7.61897 | -61.60613 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cd727e8-7882-3fd4-81b1-d3ea4d5d77d7 | -7.06629 | -59.97392 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32dda3b5-b264-3c16-a959-e26f610427b9 | -6.25624 | -55.38939 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e99f582-ec8b-3a0e-8f7f-a2768422f300 | -7.55629 | -61.18511 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README42.md)
