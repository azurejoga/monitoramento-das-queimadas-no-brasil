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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fe5d03a-e062-3a22-88a9-8086ff813ab7 | 1.33082 | -60.03815 | 2025-01-23 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 50cba362-14c6-33f6-be77-a01b6e331a13 | 1.33185 | -60.04493 | 2025-01-23 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| de030531-afef-34cb-9845-e71d6b4cb5c7 | 3.6167 | -59.95821 | 2025-01-23 04:50:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84f3568a-374c-32da-8360-e378d77cdd0d | 1.33715 | -60.0439 | 2025-01-23 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c17dd683-df21-3dae-b76c-8df0c8435d1f | -2.62502 | -48.08653 | 2025-01-23 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11395764-5309-34dd-8ad2-b8d7fddd36a1 | 1.12721 | -59.57469 | 2025-01-23 04:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08120160-648c-3c4f-912a-f5d69adac2b6 | 1.32604 | -60.04254 | 2025-01-23 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| eb06f2ce-e9be-3913-97fe-5cf0f2a8443b | 2.17617 | -61.82314 | 2025-01-23 04:50:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cb0ddc9-0baf-398d-93be-1f2f83793092 | 3.6107 | -59.95551 | 2025-01-23 04:50:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d04781-9d6d-3f26-8e06-995d40d6eea8 | 3.04351 | -60.75436 | 2025-01-23 04:50:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6155379-9092-3f4d-9747-5c78ec8576c4 | 2.1755 | -61.8187 | 2025-01-23 04:50:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bef7be62-efcc-3426-a512-968f4a34deb7 | 1.32553 | -60.03918 | 2025-01-23 04:50:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7e2fd114-5abc-3e52-8c17-20141302ee94 | 1.12767 | -59.57774 | 2025-01-23 04:50:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c244b28a-47cb-33aa-a287-2ef2849b6f86 | -6.65824 | -47.59766 | 2025-01-23 04:53:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6afa069-9944-3b3f-90b3-c04017a42683 | -1.95752 | -54.74279 | 2025-01-23 04:53:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63cb6fe1-297b-3144-91dd-91600048097c | -4.06202 | -54.70641 | 2025-01-23 04:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08a17107-2ef4-3039-a655-b27d41096e0b | -5.12412 | -56.11596 | 2025-01-23 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c4914031-14f4-3bb4-933b-7550d1ea8041 | -4.06523 | -54.70799 | 2025-01-23 04:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cbdac77f-f7e1-30e6-a094-d129ff884058 | -2.14522 | -53.64748 | 2025-01-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5d62a56-d44e-3556-b6a5-045ad0964fc9 | -6.51486 | -47.61085 | 2025-01-23 04:53:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c40be59-a2d7-3713-b6df-79517fe91745 | -7.30559 | -55.30705 | 2025-01-23 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5de2d8a-aa51-3f86-9b89-6bb2e41d9681 | -7.73503 | -55.19773 | 2025-01-23 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68262286-0092-35b5-bd89-1e8694115bc4 | -4.06172 | -54.70742 | 2025-01-23 04:53:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a48a2561-01a9-30a5-8d9a-3de23db5765a | -2.53254 | -53.95794 | 2025-01-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6eeb6f1c-b054-31f5-8d02-741f371a3e90 | -6.66127 | -47.60551 | 2025-01-23 04:53:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c35e8f1a-41de-3a42-bcee-bccfe0a1c6a6 | -6.85281 | -47.84442 | 2025-01-23 04:53:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec4ac140-b1e9-30b2-ba57-7029e23f3088 | -3.07956 | -47.79263 | 2025-01-23 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b6938a4-69d9-3ecf-afa1-0f1f7561d5e8 | -2.14179 | -53.64696 | 2025-01-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef3bbb17-0283-3499-bb8a-4ee9b14b5133 | -1.95393 | -54.74221 | 2025-01-23 04:53:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0910ff56-bc80-330a-98b1-76b9ddb50b8b | -2.66891 | -54.6013 | 2025-01-23 04:53:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| df5a0594-60ba-3634-809f-7f8ab919baab | -10.53143 | -42.43177 | 2025-01-23 04:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e24eff0c-1d6e-36cf-9bac-f709659c9c38 | -2.14463 | -53.65117 | 2025-01-23 04:53:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 611627a9-18ed-3205-b306-c82b0ed7fbbc | -6.6577 | -47.60125 | 2025-01-23 04:53:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8de07651-a384-3d94-a710-ced1f8cfe7e2 | -10.53757 | -42.43265 | 2025-01-23 04:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57577e3d-d60f-3fa8-8932-bb4adc7f431d | -11.02243 | -45.05418 | 2025-01-23 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49a7977f-a81c-33db-97e7-601d10101ed4 | -19.72831 | -54.83377 | 2025-01-23 04:55:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77edce81-5d96-30b2-8456-838eecf45d4b | -20.47674 | -53.67505 | 2025-01-23 04:55:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aef3595a-f8a6-3554-9746-ffea0a5444fd | -11.02766 | -45.05474 | 2025-01-23 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7718c3e9-a0a0-31ef-9fe7-9c75d5d12f30 | -19.73225 | -54.83058 | 2025-01-23 04:55:00 | NPP-375D | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e096c677-1a17-3b26-b65e-937617fb50f0 | -18.95521 | -53.68792 | 2025-01-23 04:55:00 | NPP-375D | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc3515f0-22c5-366f-a8fa-86558a3e8df6 | -11.02283 | -45.05106 | 2025-01-23 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ca8f4da-537e-31d2-aebd-6d5be3461c66 | -26.00574 | -51.32582 | 2025-01-23 04:57:00 | NPP-375D | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a3d0a6dd-20fa-37c1-99c7-4f4fde4cd3e9 | -27.5648 | -50.75676 | 2025-01-23 04:57:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 805f28f0-09da-38fa-ab7c-16ed9f1cdd22 | -30.41775 | -53.07111 | 2025-01-23 04:57:00 | NPP-375D | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 9133983a-f823-3eb3-adc3-2f322fabf74a | -30.41372 | -53.07054 | 2025-01-23 04:57:00 | NPP-375D | CACHOEIRA DO SUL | RIO GRANDE DO SUL | Brasil | 4303004 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 1b8a0e77-5892-327e-ae58-37c1010694c5 | -26.00999 | -51.32867 | 2025-01-23 04:57:00 | NPP-375D | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c9f7fa72-6bdf-3fc5-811c-223e63201037 | -29.64762 | -54.1981 | 2025-01-23 04:57:00 | NPP-375D | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| b5247783-8e0c-3f6c-893c-41476b25a584 | -27.56652 | -50.75918 | 2025-01-23 04:57:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f7fe4abc-9c04-3a64-a1e1-006104a09ce3 | -26.00996 | -51.32652 | 2025-01-23 04:57:00 | NPP-375D | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 74a5c1f4-f4c7-3e37-834e-981e41342555 | -26.00579 | -51.32796 | 2025-01-23 04:57:00 | NPP-375D | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 51ae7754-6ba2-34f5-84fb-272de66162c8 | -27.56702 | -50.75456 | 2025-01-23 04:57:00 | NPP-375D | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 529090f3-552f-3f90-9e19-44e67affa970 | 1.3221 | -60.0463 | 2025-01-23 05:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 93821940-27af-3c24-b27a-c8a6c189faaa | 3.04353 | -60.75544 | 2025-01-23 05:12:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f7b94ba-3d86-3eed-9457-0de4b72f1941 | 3.51255 | -60.71099 | 2025-01-23 05:12:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f5db67e-47d3-3012-b6e6-613358140a90 | 3.87582 | -59.73547 | 2025-01-23 05:12:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce70dba4-8a98-3b13-9eef-a6560bbdae41 | 1.33688 | -60.0412 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 270359fe-7d7e-36fb-8986-9226df736909 | 1.32564 | -60.03896 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f0b90213-192c-3ad7-91c2-19fea9794d99 | 1.3298 | -60.04239 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 398fc739-feaa-36aa-ab63-db972107e754 | -5.00824 | -56.1773 | 2025-01-23 05:14:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c42956f8-ab2b-3a94-b9d0-8bb23423df0f | 1.32918 | -60.03838 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fce63adc-1533-3247-9c2d-dfe139aa4606 | 2.18182 | -61.81627 | 2025-01-23 05:14:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43efd0cc-ab4e-36c6-a425-d0a25ec87847 | 1.32856 | -60.03439 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbdb2a9c-eba1-3b76-bbc6-7bc7666f9abc | 1.12771 | -59.57884 | 2025-01-23 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d31ce26-66ba-32e6-85f2-1ecaf3f54147 | 2.17864 | -61.8219 | 2025-01-23 05:14:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ee4f8bc-021e-3f51-bab7-d355732ffb1c | -5.12216 | -56.11758 | 2025-01-23 05:14:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a77ef9b9-d3d4-3ec3-b346-f4c5191559ad | 1.33043 | -60.0464 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7e63c29c-25dd-3c29-9413-5128560a10f4 | 1.01639 | -60.43945 | 2025-01-23 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77eb24dc-77c6-33d8-87bc-62227f8b738d | -6.65632 | -47.60211 | 2025-01-23 05:14:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 946dc2cb-6153-3679-ae7b-691fb44990d6 | 0.92025 | -60.43758 | 2025-01-23 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d8fee6a-8fc1-3719-aaed-917da7185f6b | 1.33334 | -60.04179 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a8d133f-4687-3fa2-b719-4e577ab79fa0 | 1.33625 | -60.03716 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92e22cbb-75cd-3800-9378-e86d5594103a | -6.66187 | -47.60788 | 2025-01-23 05:14:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 924b318f-fc3b-3c47-87bc-3e9041e96aa8 | 2.17786 | -61.81686 | 2025-01-23 05:14:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a63e6a50-9d11-3003-a460-d29823d703ff | -4.06244 | -54.7061 | 2025-01-23 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8335bef5-3a77-35a1-b5a5-7f05f3edccc9 | 0.91837 | -60.43692 | 2025-01-23 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ad93af-e8f1-3e38-a339-7a55730cddf1 | -6.65791 | -47.59931 | 2025-01-23 05:14:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcb68922-a2e5-34ea-b9e2-51f1ad87c3eb | 1.33397 | -60.04583 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5834bd31-21dc-3736-bcdc-345bc00f1c9b | 2.17389 | -61.81746 | 2025-01-23 05:14:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ccd3797e-771f-394c-9fa1-755f02dcf38a | 1.01574 | -60.43533 | 2025-01-23 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 161590be-aacd-369c-b9e9-28165fa800dd | 1.3321 | -60.03382 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7528912-6ae0-3894-9a27-3af51f755ecc | 1.33459 | -60.04983 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b64bbbf2-885c-3bc7-a484-c0e0b54e66e5 | 1.33271 | -60.03777 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b8a02e61-4d8c-31da-a7f1-10560cf91271 | 1.33751 | -60.04525 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f0cd1fb-972f-34bf-911b-ffdb99fd6056 | 1.32626 | -60.04296 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 265b932e-5c2e-3c0d-a1ba-53b7ca1d0f70 | 1.32688 | -60.04697 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 201ad7f2-7e66-329f-89e6-37d5c36d118f | 1.12712 | -59.57504 | 2025-01-23 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65c2db19-2f77-3119-a8fe-0d0ee46ab81c | 1.32502 | -60.03497 | 2025-01-23 05:14:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96fe7bdd-a159-384e-95ce-b32cc2c3cc48 | -6.65726 | -47.60394 | 2025-01-23 05:14:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 199b2d5d-1f61-3506-9581-35a90e0fb023 | -3.71871 | -53.75495 | 2025-01-23 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a08a83ff-b4c6-36a3-afc9-eef030b14437 | -7.73583 | -55.19833 | 2025-01-23 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cd21459-cfb1-3a8a-9f8f-cf672c5e2ee7 | -7.3069 | -55.30423 | 2025-01-23 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ebf44e-174c-3f48-8b14-19bd9f321538 | -10.50865 | -58.86712 | 2025-01-23 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54cd18e9-c285-3c15-abb8-2c25efffe638 | -6.21134 | -55.63902 | 2025-01-23 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c9d1ad5-e8f6-3a5d-954b-1f62e4ea3d19 | -18.95447 | -53.69066 | 2025-01-23 05:18:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d17fbe61-405f-3f41-8279-c465161da0f5 | 1.3221 | -60.0463 | 2025-01-23 05:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| f5182499-0a28-31e2-a970-49481aec2b4e | -26.01094 | -51.32841 | 2025-01-23 05:20:00 | NOAA-20 | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aa2edf8d-1e30-3486-9f5e-1152725f37ca | -26.00445 | -51.33254 | 2025-01-23 05:20:00 | NOAA-20 | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a33e8d7e-194a-3a6a-856c-85b812fcaa7a | -26.0048 | -51.32752 | 2025-01-23 05:20:00 | NOAA-20 | CRUZ MACHADO | PARANÁ | Brasil | 4106803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ab2f3720-07a8-3e73-b083-0fb263e368fd | 1.3221 | -60.0463 | 2025-01-23 05:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.8 |
| e504dab8-2de1-3d9e-bdf2-43b9912f62a5 | 1.3221 | -60.0463 | 2025-01-23 05:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |


[Clique aqui para ver as próximas entradas](README5.md)
