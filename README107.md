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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 615fd242-f8e8-339f-a5f0-4d5ea3242fed | -13.11421 | -48.22287 | 2024-10-01 05:06:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfeeb44b-58d7-3693-ba41-9a5b4da5c656 | -14.79033 | -48.76313 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0477faa-1041-388f-8413-d457f0529467 | -14.78514 | -48.76241 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f73c23bc-a33e-3e9a-a428-701e08018a30 | -14.77292 | -48.77665 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0bd16457-7ae0-3b2c-939f-548e2a14a732 | -14.77252 | -48.78 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7c38923-9d6d-3180-bdb7-53b46b2e8c79 | -14.77219 | -48.78278 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30593b55-b076-36bc-a640-3c0d62470926 | -14.77187 | -48.78544 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f66c91e-7620-3ede-8b50-131d0c3c4277 | -14.76666 | -48.78512 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ebaae419-ff4a-3238-8db2-aea67581f261 | -14.76632 | -48.78788 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 03db22c6-848c-3915-9631-678dc5242a40 | -14.76147 | -48.78453 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1e862c2e-e031-35bd-a464-a946a82eb9e2 | -14.76113 | -48.78735 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f6d716df-d340-3c0f-a82a-0fec6fa106fa | -14.75701 | -48.77777 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ee7d0f6-2905-3a17-9869-231f8976df92 | -14.75668 | -48.78056 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1cb5dc3e-f9e8-3020-86da-7cd003c3b4e3 | -14.75635 | -48.78332 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a7b82e00-f0e2-36cb-8901-0a3d9210829e | -14.75603 | -48.78605 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 61e85dab-814a-3077-997e-406ff2a337c7 | -14.75188 | -48.7767 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0bdccaf-b9e8-354b-847b-786c63e224ce | -14.74709 | -48.77268 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a171b331-6419-3484-94be-d2e6334681f8 | -14.74676 | -48.7755 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e456bf19-fe3b-35ee-9aa6-c0a74f6aaf53 | -14.74532 | -48.74267 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2da9a32d-1ccf-3d25-92be-7a2ff9b2fd1e | -14.74492 | -48.74608 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ac22467-a0c9-3173-b77e-50e2efa58aab | -14.74267 | -48.76549 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8eda8510-8c35-3796-af49-4ea3cff29780 | -14.74231 | -48.76854 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44b3553e-67ba-3d72-a1d2-ed0a857979ed | -14.74197 | -48.77148 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cf98edae-5bcf-3d45-af5e-152cbf4a6c40 | -14.74164 | -48.77431 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d67ce7e8-c152-3d83-b618-0ef58faceb73 | -14.73795 | -48.76081 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5872604a-f9c7-3406-babf-de357cf2534d | -14.73754 | -48.76431 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b3e18284-0217-3b91-9f42-f251682f696b | -14.73719 | -48.76735 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7ba0a9a4-06ac-3979-a655-c4ae16b9bf83 | -14.73684 | -48.77032 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0b2901a0-fed8-37f3-9a6a-3a441abfdcac | -14.7365 | -48.7732 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0bf201ce-6b64-3db2-bcb6-f7d30ec3fad9 | -14.73419 | -48.74776 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 310f4973-a5e7-3f15-880a-772a74dc07d6 | -14.73378 | -48.75132 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd030c5a-85c9-3568-b157-c9d39bc0aa57 | -14.73336 | -48.75497 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dffd9506-a074-3c5a-a9e5-f7e7af507358 | -14.73292 | -48.75877 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 30cf8887-4c92-3d3d-a793-8f4e1721b58e | -14.73249 | -48.76244 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9d12679e-8b01-3560-bf1a-fe687d777bc3 | -14.7321 | -48.7658 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 21501bc1-ba1b-32a5-baf0-bd8fdcc0ad01 | -14.73172 | -48.76909 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 01b6c6fd-b9ca-3f7d-a851-54fc9fb4ce9f | -14.72823 | -48.75375 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aeefe12c-201c-31bf-84a4-e572c9f790a7 | -14.72781 | -48.75741 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b045555d-503d-3455-958a-72c76a6c0e24 | -14.72738 | -48.76114 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6fe56446-4a18-3c26-a1a6-6a83be9e944c | -14.72696 | -48.7648 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d6e11b6-8cce-363c-92cf-9aad9f76c7a1 | -14.72656 | -48.76823 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d3606f9-e035-3ad5-b9c1-9911c53400f2 | -14.72301 | -48.75342 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f87e4550-3437-38d1-a368-2bf452c1acc2 | -14.72255 | -48.75736 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e3f2fd2-ba62-3caf-b093-95a7b7e41b60 | -13.72586 | -49.42346 | 2024-10-01 05:06:00 | NOAA-21 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9e352b0e-f261-3657-92c6-fe3375b27292 | -15.09471 | -49.49159 | 2024-10-01 05:06:00 | NOAA-21 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7791ce44-07cb-3298-b702-31897013b368 | -15.07865 | -48.94613 | 2024-10-01 05:06:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbcce539-0064-3e82-9424-d7f6868c99ba | -9.14384 | -48.96772 | 2024-10-01 05:06:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eca36757-12a8-39f2-b174-42a11cd947f5 | -9.04033 | -49.82544 | 2024-10-01 05:06:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a106c39-1334-3eb4-a2ae-c22ef4d7bcc8 | -9.0365 | -49.82035 | 2024-10-01 05:06:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 374575e8-4bf9-3dbc-8df7-6c1504ef8029 | -9.03588 | -49.82478 | 2024-10-01 05:06:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ba4966a-a937-3e4e-9549-b18e0bdcfc9a | -9.76886 | -50.08067 | 2024-10-01 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0b2ed9b8-a1ef-3d17-a0af-0804dcfe66b3 | -9.60064 | -50.09455 | 2024-10-01 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d5c335e-a5ef-3a2a-80ad-91c2874a5318 | -9.59108 | -50.19851 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09a15c58-14d9-37bd-adfb-39aabfd445de | -9.58778 | -50.12356 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df11bfd6-3f73-3988-a3ae-86b88ea00674 | -9.58733 | -50.12476 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cea95e57-bab5-306c-98b4-798333935db5 | -9.58672 | -50.19787 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 538c23a8-d02b-328f-a651-44ee00fdbe3a | -9.58339 | -50.12293 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e438a1d7-1406-37fa-a142-94afbae06846 | -9.57957 | -50.11795 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32805a89-1f3d-3c12-ba95-0aab773f8cf3 | -9.57916 | -50.11919 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4d71354-458a-3ad5-9243-ae30ab236efb | -9.57899 | -50.1223 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 272f004c-df78-38b4-a5a2-5d8acf07f516 | -9.57855 | -50.12352 | 2024-10-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f7ab0003-bb92-3b9b-812e-a159729a2a80 | -10.04854 | -50.3 | 2024-10-01 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efd0cf48-c0fd-38c8-8862-95fff419f849 | -10.04796 | -50.30426 | 2024-10-01 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a2022c1-9361-3857-afb3-103ac9bad8ac | -10.04476 | -50.2951 | 2024-10-01 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef409e1e-b1c3-3ddb-922a-22ab274eff90 | -10.04417 | -50.29937 | 2024-10-01 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2fd4178-ebac-37f3-b641-ffd345a497f5 | -10.04039 | -50.29447 | 2024-10-01 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8eb39fba-21ab-3464-bb97-7290d3d053ab | -10.51278 | -49.78162 | 2024-10-01 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64966539-b463-3c78-b6ec-a8d33ba33c9f | -12.2115 | -50.47536 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f89da8fc-c788-3fb5-bfc1-05e7aee0ac75 | -12.2109 | -50.47984 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c34bb6e-31bb-3b7a-b0ab-51b4d136550f | -12.20584 | -50.48369 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 692164fc-6f68-3b42-8aa3-a38af1481b44 | -12.15347 | -50.07019 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a93801a3-a34e-3af8-bdfa-bb2693e79d7e | -12.15283 | -50.07496 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ae386321-a96c-3e5a-8b84-37178df93c06 | -12.1522 | -50.07973 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c257f521-0a31-3346-b54f-01f8e6568bf8 | -12.1489 | -50.06955 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ddcf4a6c-7089-3bbe-86c2-de49c2a63741 | -12.14826 | -50.07432 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 02d506de-3b46-37fc-bfb7-1985f245b913 | -12.14621 | -50.05461 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| ff484312-3f08-3781-ad56-1e86c2e46849 | -12.14495 | -50.06414 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 89d97ed3-045f-31fa-931c-044fa1345673 | -12.13705 | -50.05332 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 64e930b7-cbd4-3819-9a85-1e301ecb5a2d | -11.92586 | -50.16349 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a565321-b240-3fcd-95e3-4eb67ff23e8d | -11.72674 | -50.00799 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29e19f7a-7887-3ada-b69c-02d6186a8fe6 | -11.35288 | -50.78944 | 2024-10-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efaee376-c7e0-33ef-9faf-7911dd72233a | -11.16021 | -49.72865 | 2024-10-01 05:06:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b9a8aba7-8d84-3152-adc8-ffb37e33e477 | -11.11467 | -49.61629 | 2024-10-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 74875e82-f911-34c2-b4b3-a232263d79fc | -11.11131 | -49.60586 | 2024-10-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f5be73e5-c5d4-3dea-acd8-a5510943c808 | -11.10731 | -49.60026 | 2024-10-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a78375da-c0c0-3af2-a422-412f18881c9d | -11.10666 | -49.60519 | 2024-10-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee08630e-12d6-396d-b0f1-454ceaf6bdee | -11.10331 | -49.59465 | 2024-10-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dfa0c392-14fa-3e16-a205-163a3804029d | -11.10266 | -49.59959 | 2024-10-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dca361f2-40fb-3622-a21a-8598eda5bc20 | -11.09931 | -49.58901 | 2024-10-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a813a0bc-72bd-37a5-b718-5966ba8402b8 | -11.09866 | -49.59397 | 2024-10-01 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 89c0a63c-681d-355c-9f82-590496ba348e | -10.98407 | -50.16233 | 2024-10-01 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c151994b-abf5-314a-aea5-733cefc1696d | -10.9829 | -50.1591 | 2024-10-01 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 79b83527-b092-30e5-8dc3-7c8cd5a4ee57 | -10.98231 | -50.1636 | 2024-10-01 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e126829e-ff4e-392d-bd40-b3d9601c639f | -10.9796 | -50.16169 | 2024-10-01 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cbcd7f7-53c8-3754-87d0-71c8cdfe2ff0 | -10.92611 | -50.08484 | 2024-10-01 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f854843-0725-3641-aad1-59a9951f96ce | -10.92551 | -50.08939 | 2024-10-01 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24d937be-a34f-3811-9eda-8e4ecccc42bb | -10.92102 | -50.08875 | 2024-10-01 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7b2c641-e5ea-3e61-abed-61a082f29296 | -10.92041 | -50.09329 | 2024-10-01 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 850eae80-00aa-3c93-b921-63727fd470fb | -12.20645 | -50.47921 | 2024-10-01 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52658a33-8dab-3eb1-9fbb-a8f643aad85d | -12.14558 | -50.05937 | 2024-10-01 05:06:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |


[Clique aqui para ver as próximas entradas](README108.md)
