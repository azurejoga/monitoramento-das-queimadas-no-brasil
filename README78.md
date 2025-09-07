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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89d0be75-904a-30a8-a86f-57e57f498dae | -5.94887 | -53.80319 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2f514143-53fa-397f-974f-c9f590f15ada | -5.96909 | -53.59554 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54537be3-1bb3-3ab5-af7b-44305e213368 | -6.29869 | -51.41129 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e723a4a5-6046-3a35-bbd9-3c20769151ca | -6.28297 | -53.43143 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39f719ca-a438-3a0e-b75e-b5aea527b0d6 | -5.97099 | -53.60021 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0a7bee2-65ad-346d-b651-ddf2b1c91c26 | -8.70135 | -54.67915 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f6ca6961-1aba-3993-9205-b093f6a49744 | -5.79326 | -57.55258 | 2025-09-07 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c67ab12-42d6-37fa-a1ea-95cf877c7dfb | -7.5969 | -61.59369 | 2025-09-07 05:38:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3deb42c5-1f6a-3ff8-8fba-a4fa0dcce923 | -6.19532 | -53.25352 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c639e585-e3ed-33d8-addc-a6cc1b539d2c | -3.90166 | -55.83937 | 2025-09-07 05:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 99fdf469-e16b-3f88-9c75-0d6df726d1af | -8.35105 | -52.55614 | 2025-09-07 05:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 72a8a25b-959a-3435-8674-38fb14a592ec | -8.62659 | -54.65306 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 719cf1fc-2857-3b85-9898-ef4e5b3912c7 | -5.97201 | -53.59272 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0be0c56c-5147-3cc6-92b8-326893ca7d35 | -8.62706 | -54.64948 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7481fe01-beaa-30e5-9dcc-8bfd98d6cc72 | -9.39452 | -54.76373 | 2025-09-07 05:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57889a3e-e93b-3e88-91b3-46fc4f48e890 | -3.32763 | -54.9091 | 2025-09-07 05:38:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 631f3714-7850-304e-bf59-514f68c267a7 | -8.69594 | -54.67781 | 2025-09-07 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9759c272-4177-30cb-8cf7-a817161218d5 | -12.9477 | -54.793 | 2025-09-07 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e85c896b-c85a-3452-8760-f8149f2b5940 | -12.9482 | -54.7519 | 2025-09-07 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ce6c0c57-9fe4-3c64-b59a-e295f83056ed | -12.7153 | -56.5632 | 2025-09-07 05:40:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 5efae2ab-2c21-3f41-9127-49894015943a | -12.948 | -54.7724 | 2025-09-07 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 196.4 |
| 5354cede-2104-3675-93ef-15b27c35b6d3 | -12.9289 | -54.7744 | 2025-09-07 05:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 85a1cbcd-4d7d-383b-8f81-c8bc88fd8b39 | -13.896 | -54.0092 | 2025-09-07 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 09a2944b-4434-3823-99dd-a2c6fd05a41d | -12.8055 | -48.0182 | 2025-09-07 05:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| a3e24747-be14-395e-abcd-bff096906c3c | -13.9153 | -54.007 | 2025-09-07 05:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d91ac3e2-d707-3173-adbe-2501fa3b4a19 | -11.72386 | -55.29707 | 2025-09-07 05:40:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c787e427-df82-3069-8ef9-c67aba6f79c9 | -12.81397 | -52.91031 | 2025-09-07 05:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31adf47c-a39c-3483-92d6-b88f13167ccf | -10.87972 | -55.72602 | 2025-09-07 05:40:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f5299e7-2ed4-3ab1-8b35-8d8b85d48bdb | -10.17035 | -61.14254 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f4754e95-71e0-3e11-8f32-df636d94a6fe | -12.9281 | -54.76817 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7bdcfbeb-08ed-3f61-8923-d034adc711f6 | -13.91678 | -53.97549 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9db3e64e-7eba-31e9-aaef-913029238c3f | -12.93386 | -54.76905 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 88e21681-480b-305c-bbd8-5dd3f3a72f07 | -10.15564 | -61.14061 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e4c5a35-0e19-3bf4-a8d6-07d5c97844d9 | -12.87283 | -62.10728 | 2025-09-07 05:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 31493db4-d750-3bde-adb7-9e5774e39116 | -13.93683 | -54.01849 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b1797c80-32db-3029-a6eb-76d88668537c | -15.69481 | -53.55956 | 2025-09-07 05:40:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 09179161-45d0-35ee-86da-ae3969661643 | -12.93433 | -54.76495 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bf20f6bd-ec17-359e-a168-fa62d0ea29dc | -14.35412 | -60.32457 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01da512a-ae55-3689-bb70-dfd2e0c7b1be | -12.64266 | -56.98248 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f842584e-1b30-329d-9ef5-81876f64f35d | -13.90638 | -54.01282 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6a09c9cb-0221-3907-9672-294697ea3606 | -13.94266 | -54.02184 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 005c068d-8fbb-3bdf-b414-eaf347ef209a | -11.04431 | -54.17293 | 2025-09-07 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eff6af0a-a897-31c6-93a3-a992ee4c503f | -14.42527 | -60.19713 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c2a31c4-a7f8-3580-8757-1fa3bd79836c | -11.20235 | -55.0531 | 2025-09-07 05:40:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06e50f36-9b6c-36c3-a124-08acf7520290 | -12.35715 | -63.64222 | 2025-09-07 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33d7c15b-60fc-35b1-95cb-f9c6074461c9 | -12.71941 | -56.56674 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 8df88d18-6d5c-33b7-a377-619bb858c8d0 | -11.22193 | -55.02085 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 420241ab-a326-3252-8e14-8aff1305c9df | -9.78277 | -63.152 | 2025-09-07 05:40:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5cb700d6-661a-3a04-ba55-a6e35244167d | -11.20759 | -55.01279 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02cb1a25-1e57-337c-8aa9-cadeb7753c5e | -14.42116 | -60.19662 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1eec4e0f-5b0a-3c23-a6ff-1db8503c401d | -9.43174 | -62.36681 | 2025-09-07 05:40:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5bd610e-3061-3c0b-a753-47b7892c7644 | -12.4221 | -63.89843 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8becbb2e-8271-30d9-8606-411152ce6513 | -9.965 | -65.2375 | 2025-09-07 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3c8f748-e544-30fb-a650-6538b578cc4e | -10.8438 | -55.09937 | 2025-09-07 05:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b19fd3e3-cd00-3aa1-ad46-f7165976e8e4 | -12.9281 | -54.77036 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2e772190-19b6-3d28-a08c-29ec9cce6f8b | -12.4148 | -63.90099 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dd75c02-85f8-3030-b25a-fef5ac1de2c8 | -12.94976 | -54.78353 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96726c69-377d-34fc-ae95-a8ac305cffc7 | -12.80777 | -52.90969 | 2025-09-07 05:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 287dd0ba-e498-358f-ab3b-a046c59249b9 | -11.16847 | -59.15867 | 2025-09-07 05:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b026df83-df9f-3a51-9d39-d4eb9462f498 | -12.86923 | -62.10674 | 2025-09-07 05:40:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5380a998-4de7-3d87-8c7a-099d1bd58cba | -12.95602 | -54.78011 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 54e99130-d9a9-3670-8b76-34b078110273 | -10.42381 | -60.74786 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5332335e-7d5f-3da4-ada5-2964cb12bd3d | -14.35117 | -60.3203 | 2025-09-07 05:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ff50034-9c49-312b-a5d1-813bd06323a7 | -12.93435 | -54.76717 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f0703baa-0655-3ce1-b80a-da90da13ef1d | -12.93385 | -54.77125 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f7d38d16-f994-398c-a69f-02e8c33c08ed | -11.0507 | -54.16941 | 2025-09-07 05:40:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e7790593-af68-3883-b489-276fef4def0a | -13.77811 | -52.77856 | 2025-09-07 05:40:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b1e5b0f6-7c66-3ab4-a472-4a8efa077de8 | -11.64545 | -54.53968 | 2025-09-07 05:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a21c8bc-b0a5-3d7d-9f90-0b926f261afa | -12.94445 | -54.77878 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| ce72da1e-da6d-34c9-8bf1-1670f8fc6729 | -12.93335 | -54.77532 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ae81891d-b6ad-324f-a248-b09162f1808d | -11.21172 | -55.01207 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b137af5-47e3-3f78-92ca-3d45405081f5 | -12.82127 | -56.52171 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a49740a-255f-3cd7-bf48-d52f1d85b7be | -12.42154 | -63.90205 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76fff13c-80d0-3f47-bcee-9c4567a6abdb | -9.35504 | -65.41963 | 2025-09-07 05:40:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14e8b765-ffd4-354e-ba7a-5603a30abdae | -12.93868 | -54.77805 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0366dda2-c7d6-3078-8ddd-a685c62139fd | -13.93649 | -54.02144 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e83b1f57-1285-3c5e-a10d-b7b462428fcd | -10.56915 | -61.23497 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4fe7424-6085-3c77-b430-0b8b416ac26a | -12.41817 | -63.90152 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 635f16b4-ba99-3ef8-a840-9a26baff8913 | -12.35828 | -63.63488 | 2025-09-07 05:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec9abbe8-80ca-3833-9739-377a9c6d1e64 | -12.41144 | -63.90045 | 2025-09-07 05:40:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01499ece-9a2c-3dca-80d7-e988ed57ee35 | -10.58188 | -61.25055 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c7472fb-6cf8-35a9-9dc3-25b3c78675e1 | -11.21774 | -55.00903 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adec7097-fc01-326d-8373-25c125bc65ba | -12.62702 | -56.98574 | 2025-09-07 05:40:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 370b6218-7318-3ffc-9537-6eef76d08a2b | -11.20711 | -55.01651 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d922b14-a4c3-3ffd-96bb-7de67e060e4c | -16.33053 | -58.11744 | 2025-09-07 05:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ecb03bed-4255-30f1-a83c-99192c342014 | -12.81334 | -52.91575 | 2025-09-07 05:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b16a5da-a582-3a27-8101-f88051a5b0da | -13.936 | -54.02577 | 2025-09-07 05:40:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b8964fb9-3f10-3b22-ae26-b0de2218f482 | -10.16489 | -61.1285 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a0e0f5a-bcd9-3f8f-977b-61e4920a821e | -10.57458 | -61.24921 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 79c55b9e-7c86-3f3b-95d3-9151a429f406 | -12.82164 | -56.51868 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40711d17-c8e7-39ae-a8d8-9276223219ee | -12.9454 | -54.77063 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 19234084-814c-3b65-90ef-f1e6e2e38dcd | -15.84157 | -52.27513 | 2025-09-07 05:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7cfd2fe9-79e1-39c4-b356-251579ac2115 | -15.70289 | -53.55485 | 2025-09-07 05:40:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3e359229-1ec0-3e95-a396-529015d7aa1d | -10.57397 | -61.25343 | 2025-09-07 05:40:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4dbde0a8-fde6-3683-a672-dcd04b65dc4e | -12.71467 | -56.56303 | 2025-09-07 05:40:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 64966dab-02db-3787-9db6-8091560acfc1 | -11.32071 | -55.21746 | 2025-09-07 05:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 325b1d08-84ae-355a-ab4e-bce1d08ac33e | -10.83786 | -55.10207 | 2025-09-07 05:40:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4148cadf-37f4-31a4-82e7-1511b95e2c86 | -12.9512 | -54.77121 | 2025-09-07 05:40:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 54382f85-716c-39ca-99ec-cce6d9505961 | -15.8347 | -52.27363 | 2025-09-07 05:40:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4acaf094-bfc3-3874-9e70-f32ba58cc7b1 | -12.78252 | -52.95582 | 2025-09-07 05:40:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README79.md)
