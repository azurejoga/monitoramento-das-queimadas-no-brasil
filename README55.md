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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98b8ead7-cea6-3f62-accc-8c9ec8fc9457 | -6.62571 | -58.50506 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c41fb02-0ef3-3bbf-91ce-a9ab1cd309bb | -8.21514 | -55.00992 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 510b7796-e1fc-316b-85bb-5237dc408c95 | -6.91879 | -60.06891 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5e21d848-001b-31fc-81a8-ed6d8144b55f | -6.65286 | -58.49848 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c9ed204f-646d-3c02-87c7-7f0ae771a724 | -8.16656 | -46.19613 | 2026-08-26 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c712c50e-e321-3244-9e14-89a387e2bb01 | -3.62585 | -49.69931 | 2026-08-26 05:27:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a0c9dcd-588a-3e6a-b73f-b587f25fb4ae | -5.347 | -45.15897 | 2026-08-26 05:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 870f1ca3-402e-3f13-aaf5-618d171a328d | -8.17149 | -54.95362 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 629352b8-6d27-39dc-a8c7-dc6c94cd75d7 | -6.80045 | -59.45158 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a417495-a17b-3a78-a007-27f907a7392c | -6.62736 | -58.49459 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ce5629da-c36d-3841-9e1e-b744f91c6b1d | -6.51113 | -55.22421 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6d21a76-8f56-38fe-9f20-8ede4c014e09 | -8.56666 | -54.81668 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16f56658-065f-31d6-b391-3a3cd120c694 | -8.62585 | -54.73199 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 044561da-a4bf-3e57-8fd3-3aca13b018fe | -6.9746 | -59.08091 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bd7c48c-0444-3634-9f00-08462300651a | -6.78715 | -59.6386 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46353403-447f-3094-8f19-7f0447e3e968 | -8.01577 | -51.80899 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23289e77-e96b-3eec-8052-834eaac105ec | -5.95429 | -53.58604 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 666f69e2-2ee6-324e-b980-2fde73c43ae1 | -6.81605 | -59.45768 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82f532e4-3791-3f47-8b3b-91014a898411 | -7.56388 | -61.42608 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbbd173d-6756-3872-b15e-0e32f8c094e9 | -6.30216 | -53.56869 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74cc620f-e8dd-3fba-b24d-ece6863fe08a | -5.95375 | -53.58969 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de9113b0-926a-335e-be01-6a71adbfd7d4 | -3.06957 | -61.07721 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4ca8eba-4652-32c7-986b-d373b85cd3a3 | -7.47215 | -61.37992 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c918e5fa-1ba2-31c4-8bdf-eba5951d017c | -9.01784 | -50.77409 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f407a70-bd6d-32cd-ba4f-332c7ae6171b | -8.51469 | -55.35281 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28afb0a6-ef01-36e1-ae40-88d0d6d50599 | -7.07416 | -59.21807 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 726ea01c-13dc-3570-ab3f-2309045acb4b | -6.86087 | -59.71116 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ab84a3d-d75b-3ed7-a11a-e467a6b391b1 | -6.76004 | -59.44871 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8815d49e-99d7-3840-9452-143405767d9d | -6.69369 | -58.7157 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d855f2fd-a6d6-3496-b2dd-368e5b503db4 | -6.82544 | -59.42008 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 28fa7d24-5de3-307b-91de-b68490944569 | -6.94305 | -59.31756 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc7718ff-6055-3d50-b6f3-2a916fe62bb2 | -8.57381 | -55.28513 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74723b14-1fe8-3967-ac61-1124a53830ec | -5.78044 | -57.55147 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 438335bd-42ab-3bb7-be12-4786d71ab697 | -8.20206 | -54.96339 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a57d14e-32e0-3cdb-bd33-2f1525816f5f | -6.78483 | -59.73835 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b35b048d-72d8-392b-96b5-7d97c0b31869 | -8.16855 | -46.19242 | 2026-08-26 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9efd52a0-cd08-310b-b8da-7f3b1d4fa6ed | -7.51336 | -55.5841 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 721a699a-edca-3f53-bc6a-3609e6b33f07 | -2.50278 | -48.1408 | 2026-08-26 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ae3a7be3-11fa-328f-ad56-2caa9eda6c99 | -6.82486 | -58.65839 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c7f630a1-e5dd-382c-a1b3-9c98320d4d9f | -6.81323 | -59.60348 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a05eac8-9446-371c-b5af-b06896b43d13 | -9.02777 | -50.77993 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 073378b9-77e1-3080-8a98-61ec83bcbf0e | -5.93731 | -57.73365 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edf6234c-605f-37b7-baf9-60db9f3eca4a | -6.14193 | -57.69887 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd11001b-9c4e-3d32-839f-128927c345da | -6.97894 | -58.3234 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eeb6c02f-e005-33ec-b77a-bfaeac33f04f | -7.38368 | -55.15682 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e7bd91d3-60ef-36bb-b5a5-88c5073e03e7 | -4.74876 | -62.81275 | 2026-08-26 05:27:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a00aa56b-147e-3b4c-9422-d0079d0681fa | -6.72627 | -59.44689 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f05ab4a5-ee74-382f-a4df-eb7ebc5b982d | -4.45371 | -55.49214 | 2026-08-26 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94afb092-6061-34ba-87af-54abdd2deae3 | -6.26506 | -53.38047 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc68abfe-384d-3712-85a4-bab05efda428 | -6.11887 | -57.69162 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96cb5d32-dfcf-3327-9aa2-16916c076c0c | -8.17855 | -54.96007 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 69533f70-3dff-3d98-a542-b0913bef2148 | -6.22601 | -55.47472 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 51221c2c-a9e4-34a9-9c9b-2dc745031a5b | -3.93445 | -59.33519 | 2026-08-26 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0239ede7-a9a5-3e20-993e-af5dd1e03993 | -7.39512 | -55.15874 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00ed8052-a5c7-3d62-93d1-972b2bf5575a | -6.69591 | -58.72318 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8bbfe2f-cc3c-377b-b460-114114fd4da4 | -6.64843 | -58.50494 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 4b129b82-42e5-3d45-83e0-1eb9c7deab58 | -3.07203 | -61.2128 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e14fecbc-0862-3cf4-bf45-3a5c0aa081c9 | -7.21365 | -60.60931 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ad083e4-ec65-330b-b509-a21931a2ba61 | -7.39203 | -55.15323 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56c56926-4503-386b-8c87-3708f0063df6 | -9.0422 | -50.79187 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6760a7a2-427a-3e98-b044-ff6ef3552b50 | -5.98362 | -55.71547 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e5dc598-7a10-3bb7-a1a5-9688d292e395 | -7.0105 | -59.23578 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e9dfc38-0a49-3f7c-9341-11009efecf36 | -6.15234 | -59.9288 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73bce917-b6c3-3f4b-af36-979892178d77 | -6.72073 | -59.43889 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e2db19ab-9a1d-31fe-b74d-78f009e1e212 | -8.58022 | -54.83468 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8912d63f-2434-35b2-a720-0c4bf7fe38e1 | -7.39443 | -55.16347 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 49bcf5b5-4e75-3d43-a33f-905e0aafd018 | -6.64346 | -58.5149 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 91b83edb-c351-347d-aafa-c1bfab157fe3 | -8.57523 | -55.27547 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40474b34-9f08-3894-ac6f-8927b05c59fa | -6.26927 | -53.38112 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25da87ec-ae31-3d82-a189-dcb6463cc2b9 | -7.02101 | -59.23389 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab7568fe-bba1-3f87-9304-c56519df3396 | -6.6207 | -58.49353 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 517bc9a3-c37e-370c-b767-94dd0ef509ad | -8.99495 | -52.39045 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| adc7e975-b4af-35ab-9689-3846d93a8af6 | -6.96686 | -59.08679 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19bd34f3-c4d5-3e86-80d1-b7651e7434c9 | -6.93669 | -62.88824 | 2026-08-26 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78e9d076-6772-37b0-92e3-95b4b72479b7 | -6.79102 | -59.40384 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da8ebeb8-1b7f-3c1c-ac58-2d46de05517d | -7.07306 | -59.22501 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 83eb8499-a973-3677-8ebc-d05a5165449f | -6.93817 | -62.87934 | 2026-08-26 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffa3d3ec-3ef3-3259-96fa-42efc5ce9935 | -6.17821 | -55.44048 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b1ab997-f33d-31b9-9c10-f80f84ddb661 | -6.72226 | -56.34258 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2f7cc81-5254-3ae0-9d2e-4c4e2f42bfdc | -6.32767 | -54.7352 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3433aa2f-6c80-3492-ba6d-3681558a1d28 | -7.34809 | -55.65495 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8cfc1d5b-14e4-3cd2-80c5-88b8dd75386b | -2.49709 | -48.13985 | 2026-08-26 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21f7aab7-bc50-3fc7-bcd6-a1de7acfe490 | -6.41138 | -60.06014 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cec9981f-f5fa-34fa-9ef8-870ad55f9dda | -6.41081 | -60.06368 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26a44fdc-7255-3f04-bd7b-acb93b42c5b0 | -7.6089 | -61.19073 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df613d90-2b8d-3efd-8e82-96d15d81274f | -6.64674 | -58.49392 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 55a26873-029b-376a-a515-01f05ec57f8a | -6.12245 | -57.82399 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d364814f-fcda-3ca1-a2a1-81f3d8412ace | -5.77594 | -57.55813 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4b16d21-ebdd-32fb-8822-54de16624ab5 | -6.8335 | -59.94727 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3238fa31-6c60-32b6-b260-fd27d3ff42a3 | -8.76739 | -49.96724 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bedfcd86-853f-3632-9131-934bfd43d9e1 | -6.84465 | -52.50518 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd17cdaa-e62c-3d0a-b751-703a49aba72f | -6.20009 | -55.64278 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af4b4c93-3afc-3d80-95d9-40329c4d53ba | -6.26141 | -53.37595 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6237be96-3ed3-3974-9580-b22cc2f8dc3a | -6.14025 | -57.70964 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cba6cc41-8f1f-3460-9d72-e758d36f83ca | -7.5171 | -55.58464 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4b1fd89-172c-30e3-b6a4-2627cad7f785 | -6.72959 | -59.44742 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d67be12-86e4-316e-8125-dd40a21e6b5c | -3.12731 | -61.18844 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc606f48-66eb-3246-8378-ede75f783636 | -8.58644 | -54.83761 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58324e19-75c4-3c14-9c34-9b8b7b9e4da5 | -6.98894 | -59.26437 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98da17bc-1b77-3a26-bd30-b2dcccf05628 | -6.61001 | -58.38789 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README56.md)
