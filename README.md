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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7950ec58-f43c-3e17-b5e2-9068fd92cb7e | 2.8712 | -61.1094 | 2026-03-09 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 59551fa1-15d7-32b5-8893-d5cc36dd377b | 2.8714 | -61.0527 | 2026-03-09 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 68.0 |
| f636c95d-19a9-3c30-aa97-8bfeb07879f2 | 2.8713 | -61.0716 | 2026-03-09 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 105.9 |
| a2040127-430d-3237-9fd9-bff41286b6a5 | -9.8146 | -36.3074 | 2026-03-09 00:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 132.3 |
| 85b494a2-b74c-38a0-b8b9-4745774901e3 | -9.8141 | -36.3344 | 2026-03-09 00:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 142.6 |
| 6471391d-6385-36a8-bcb1-eb78d82efb89 | 2.6905 | -60.2591 | 2026-03-09 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 3240db20-c6ea-3c87-9fb0-9e602a975696 | 2.8713 | -61.0905 | 2026-03-09 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 155.9 |
| ca9548d0-b93a-37f7-8f93-4058e0865352 | 2.853 | -61.1097 | 2026-03-09 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 65.3 |
| dd98a97e-fa81-3087-98d1-adbcc88eac77 | 2.853 | -61.0908 | 2026-03-09 00:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 5b3a778d-87d5-3994-ab98-497c3191c2fe | 2.7087 | -60.2588 | 2026-03-09 00:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 102.5 |
| e0659721-089b-3c43-8cef-3d0d5fdbc789 | 2.7087 | -60.2588 | 2026-03-09 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 112.5 |
| 39e93d04-b255-3aa3-a312-3db3c906cb1f | 2.8713 | -61.0905 | 2026-03-09 00:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 29c1d635-015f-3252-9ee3-33c74a6001af | 2.6905 | -60.2591 | 2026-03-09 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 144.9 |
| 071b272d-9ad9-3ec5-b56d-7704d37df6d7 | 2.8712 | -61.1094 | 2026-03-09 00:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ab5411c0-ad38-3092-940d-b064018bac50 | 2.8713 | -61.0716 | 2026-03-09 00:10:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 99f5d63a-2804-3167-82f9-4cf47d167da7 | 2.6904 | -60.2781 | 2026-03-09 00:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 39c34620-4b11-388f-9530-0828e3156474 | 2.8713 | -61.0905 | 2026-03-09 00:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d6b46d29-26d1-3d52-9332-fb604557e236 | 2.6905 | -60.2591 | 2026-03-09 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 5cf19000-ba91-3d51-b01f-f6e841c7bf5e | 2.7087 | -60.2588 | 2026-03-09 00:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 94.5 |
| c8d304bf-ffb9-348a-86af-eb21fe99652a | 2.8713 | -61.0716 | 2026-03-09 00:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 46d59b7d-544a-3745-bcb1-0ded4e5aced5 | -16.6146 | -46.41559 | 2026-03-09 00:22:00 | TERRA_M-M | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| b2ae7b79-78a9-315d-b3a1-63d1a44166cd | -3.41963 | -48.33675 | 2026-03-09 00:24:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 09633169-7a2f-342d-b6ac-c348622536c7 | 2.68942 | -60.28489 | 2026-03-09 00:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 24.7 |
| d3a8d6b6-b192-3e30-90a3-7c8d7dc9373d | 2.314 | -60.22245 | 2026-03-09 00:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 26.9 |
| cc6e7337-1942-3214-873a-97d456d4aaaa | 2.70741 | -60.26169 | 2026-03-09 00:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 5bf4d672-6aba-3bd7-9b7f-546d134662fa | 2.87454 | -61.08344 | 2026-03-09 00:26:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 33.9 |
| fbe68a42-cacb-3942-ade3-8663da0c18e6 | 2.73559 | -60.36973 | 2026-03-09 00:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 8771027f-2e35-36f7-b671-ef2f8e91db8e | 2.72365 | -60.37323 | 2026-03-09 00:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c5968871-70ce-3019-a30f-f4c685fe3e95 | 2.72753 | -60.34769 | 2026-03-09 00:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 20.7 |
| b2ada912-86a6-3eb4-a917-4750a51a5b9f | 2.95332 | -60.16321 | 2026-03-09 00:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 16.3 |
| db436ee8-691d-327d-8968-50be28781501 | 2.69316 | -60.25962 | 2026-03-09 00:26:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 125.5 |
| 89238f09-bf96-3093-9ae4-bbfd89a983f3 | 2.31686 | -60.22884 | 2026-03-09 00:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| b6ea12d0-0ee6-3e8e-8969-9d1b7e2f4dc2 | 2.6905 | -60.2591 | 2026-03-09 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 113.0 |
| deabc8cc-33da-3e5f-85e9-95d5d26860ca | 2.7087 | -60.2588 | 2026-03-09 00:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 85.4 |
| d28db936-6e20-3541-989b-b998a66fc6cd | -10.0082 | -36.2463 | 2026-03-09 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 81.1 |
| 25315c37-e23f-3bec-a965-4244567818e6 | -10.0077 | -36.2733 | 2026-03-09 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 94.0 |
| 5dbad3e6-4cdb-39f8-a332-c2ffa31fd3c5 | 2.6905 | -60.2591 | 2026-03-09 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 96.6 |
| fd46d3a8-2765-3f5f-b0b3-de44aad20195 | 2.7087 | -60.2588 | 2026-03-09 00:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 106.8 |
| a2b1ba6b-1b22-3408-996e-b96d50022381 | 2.7087 | -60.2588 | 2026-03-09 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 22108b22-6a40-32fa-b186-ec2d52b19d61 | 2.6905 | -60.2591 | 2026-03-09 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 9d6b4bd6-7365-3d7e-871d-43f5b6f9975c | 2.7087 | -60.2588 | 2026-03-09 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 93.3 |
| ec1f8ebf-070f-340e-a025-5c229774b71d | 2.6905 | -60.2591 | 2026-03-09 01:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8beb264c-8bd3-332f-a73c-1667470c5b8a | 2.6905 | -60.2591 | 2026-03-09 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 40f33027-4906-3a29-b09f-5e55e8405fe7 | 2.7087 | -60.2588 | 2026-03-09 01:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 104.0 |
| a80ce7cc-f868-361e-8111-ebda35c7104e | 2.6905 | -60.2591 | 2026-03-09 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 2173bf32-0c82-356b-a3b5-93cc46930ade | 2.7087 | -60.2588 | 2026-03-09 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 93.3 |
| ca123d0a-a3fe-30a7-88f0-c53644fc8766 | 2.6905 | -60.2591 | 2026-03-09 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 1780d38d-7110-3fae-987c-0894611b1abc | 2.7087 | -60.2588 | 2026-03-09 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 95.8 |
| f92872ad-038e-38a9-9ce6-be59744c8ff3 | 2.7087 | -60.2588 | 2026-03-09 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 6c04a96f-83ed-340b-b0a7-8fb07182ed42 | 2.6905 | -60.2591 | 2026-03-09 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 9ccf80ad-94de-3b13-bb3c-f3aa86d0079b | 2.6905 | -60.2591 | 2026-03-09 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 6017918a-a720-38fd-844f-6d9295d29ed8 | 2.7087 | -60.2588 | 2026-03-09 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 11320f4a-dc0e-375f-9a7a-56ea9da043e2 | 2.6905 | -60.2591 | 2026-03-09 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 5811188c-a60b-3798-a355-03cfe5039c3e | 2.7087 | -60.2588 | 2026-03-09 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 3c4bb785-570f-3093-aab3-aabffc1a4dd7 | 2.7087 | -60.2588 | 2026-03-09 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 6e5a1b26-c396-349b-b96f-592f0f76aece | 2.6905 | -60.2591 | 2026-03-09 02:10:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| bc492490-407b-383a-9832-206a8f030d79 | 2.6905 | -60.2591 | 2026-03-09 02:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 5062a97e-604a-3492-aa3a-cebbf395f4c2 | -6.5631 | -51.1126 | 2026-03-09 02:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 7da8279c-3b03-3e27-83e9-4e6a8a9e5b54 | -6.5631 | -51.1126 | 2026-03-09 02:50:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| eb207c54-da9f-35c4-a3bc-7a03274b9160 | -10.75461 | -37.18448 | 2026-03-09 03:00:00 | NOAA-21 | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 36d97db4-420b-3b75-8cb1-ecd36caa022c | -10.74829 | -37.18339 | 2026-03-09 03:00:00 | NOAA-21 | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| db5c071a-076f-3c76-8f51-0b85ab54892b | -10.74728 | -37.18846 | 2026-03-09 03:00:00 | NOAA-21 | RIACHUELO | SERGIPE | Brasil | 2805901 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 488a3746-8d0a-3f06-9dcd-4102ee53892f | -6.5631 | -51.1126 | 2026-03-09 03:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 547ced4e-98c8-38b4-8992-b76824f67757 | -4.71149 | -38.45118 | 2026-03-09 03:28:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 86e0bbc7-2fc3-3dd4-aa6f-070e4ba69c02 | -4.70639 | -38.45033 | 2026-03-09 03:28:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 938cd0ea-15c0-3f65-b57c-762b75cd2517 | 2.8713 | -61.0716 | 2026-03-09 03:30:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 94.2 |
| e71ac230-f079-3273-89d9-7e5e50d02c5c | 2.8713 | -61.0905 | 2026-03-09 03:30:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 80001567-78de-3d9c-b96e-584c1eacbc51 | -6.05457 | -35.44964 | 2026-03-09 03:30:00 | NPP-375D | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 55a57dac-07a4-3fe7-ad49-02fc7106469a | -6.05502 | -35.44903 | 2026-03-09 03:30:00 | NPP-375D | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b6404dc-a350-394b-851b-19acd5c6c71b | -7.92023 | -37.62979 | 2026-03-09 03:30:00 | NPP-375D | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7d0f3d65-74ca-3c7e-8274-5709781915a1 | -11.57296 | -37.52919 | 2026-03-09 03:30:00 | NPP-375D | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f04ec3d2-d0fe-346c-9e2c-66226a3d6b8e | -17.60929 | -39.75305 | 2026-03-09 03:32:00 | NPP-375D | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a4b543d9-dba3-3de2-bf67-76a5070259f8 | -16.92556 | -39.3785 | 2026-03-09 03:32:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e2db7af8-31f8-3e81-b41d-964db98acc6e | 2.8713 | -61.0716 | 2026-03-09 03:40:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 8223b128-85d8-3546-954d-c54a70d98478 | -4.70923 | -38.44993 | 2026-03-09 03:49:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1aedce6f-fda2-3739-b22c-58ce4b533a41 | -4.70982 | -38.44622 | 2026-03-09 03:49:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ebda3a64-cd06-3c30-abc8-cfca0d0fe9b7 | -9.61351 | -37.0517 | 2026-03-09 03:51:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b10bb0a4-4d7a-3524-878a-5a8df1407bae | -9.47131 | -46.08431 | 2026-03-09 03:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0d713316-684e-3168-ad89-b8dd9c56becc | -9.61074 | -37.04767 | 2026-03-09 03:51:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c6b1e61b-0e4c-3bf8-a919-ecf10ebbe584 | -15.3844 | -43.58556 | 2026-03-09 03:51:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 409925b9-2b71-3c96-bdc1-4e0b77318ac6 | -9.61019 | -37.05117 | 2026-03-09 03:51:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 743963b1-e455-379e-907b-578b445d56c9 | -15.60659 | -42.02034 | 2026-03-09 03:51:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5b7ac3fe-6fde-314c-956b-7217853e5c45 | -9.47581 | -46.08829 | 2026-03-09 03:51:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b41033b2-d284-3cb7-9418-6a29495a83bd | -17.61211 | -39.75164 | 2026-03-09 03:53:00 | NOAA-20 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 17f51be0-7ed7-3b91-a261-75bc194b104e | -20.08161 | -40.20375 | 2026-03-09 03:53:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 085bdf69-dbe0-39f1-a006-0502fc7dffeb | 2.8713 | -61.0905 | 2026-03-09 04:00:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ff0ef28b-7b45-3b3a-a1a2-2fbf405c6fe4 | 1.7049 | -60.2901 | 2026-03-09 04:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| a9512bfb-2741-3653-8a3a-dc54a2312237 | 2.73165 | -60.35883 | 2026-03-09 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b1f374be-1590-39a0-97e9-c79bf22c6274 | 2.3208 | -60.22238 | 2026-03-09 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0f271ff1-37c6-3071-a1e8-40631e1be8ed | 2.72488 | -60.35988 | 2026-03-09 04:38:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 89e7370d-e2dc-383f-b289-43d8d27fc23c | 3.49034 | -60.75848 | 2026-03-09 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48c24ca1-dc0b-3367-9362-4773e2a5c495 | 3.49133 | -60.76516 | 2026-03-09 04:38:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c68293ce-4c6e-3555-bc73-c4e139e99b87 | 2.69528 | -60.2526 | 2026-03-09 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 75ebd395-458b-3171-8b18-6bdef1a653f3 | 2.70095 | -60.26436 | 2026-03-09 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fd78ac4-2e46-3fec-927d-16601676e70d | 2.70875 | -60.25055 | 2026-03-09 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 236a8158-025e-3771-bf1f-0815cdf1d2fd | 2.69911 | -60.25242 | 2026-03-09 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1d3424a2-0595-337f-8a47-a65244efc43f | 2.69704 | -60.26456 | 2026-03-09 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3efd9c72-1877-37d5-a396-44271a5a4831 | 2.6942 | -60.26533 | 2026-03-09 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aee7664a-7225-3b38-81a7-dc1e9289ddc4 | 2.86861 | -61.06048 | 2026-03-09 04:38:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5a522126-002b-3403-a395-b51ba0075c65 | 2.86534 | -61.06857 | 2026-03-09 04:38:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README2.md)
