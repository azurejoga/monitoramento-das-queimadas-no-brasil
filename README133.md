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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a84b514-4e2a-35eb-bf21-b3bdfb7686ad | -11.21166 | -60.23457 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1b056f5-b136-3940-b007-6889380d9d1c | -11.15715 | -60.22966 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6082468-3956-32ae-8fca-5e2495e7c1fc | -11.15605 | -60.23689 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6537856-355c-378e-b788-dc0c9aa4340c | -11.15323 | -60.23273 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 012845b9-a82f-3825-8d93-ab8017381510 | -10.60808 | -61.64895 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0c061e4-279c-3aa5-9a80-70b180b79f49 | -10.60475 | -61.64842 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60d4080b-c7b8-36b4-8411-458dcabecb47 | -10.33036 | -61.65464 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 995f1867-4a45-37de-beea-c227e2778876 | -10.32759 | -61.65059 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d26b2dc-c1c7-3a1d-8905-908651c3042d | -9.97258 | -62.58345 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 232bbd54-3d6f-3b5a-9c33-6f60180b8a25 | -9.9692 | -62.58289 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 400a4f3a-11e2-3031-afd4-b281489a64c8 | -9.96582 | -62.58234 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a4543130-8ef1-37b2-b9fe-3f0ca5fc499c | -9.96244 | -62.58177 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6ea6834-9c6b-3716-a3bd-d48638abc90d | -9.93005 | -62.25786 | 2024-10-12 05:25:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b53947e6-8664-304a-866d-5a537de86e72 | -9.92948 | -62.26144 | 2024-10-12 05:25:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93716465-9ecd-3a0e-acb7-3774b1955829 | -9.75581 | -62.36976 | 2024-10-12 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 150d0a24-285d-3bd6-898c-bc7fd48fe1c4 | -9.70777 | -62.32496 | 2024-10-12 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 908b769c-4c95-34fd-9325-8bb8a25d0137 | -9.7044 | -62.32441 | 2024-10-12 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5680ada6-43ed-3c42-9974-abc3fd982c64 | -9.645 | -62.10563 | 2024-10-12 05:25:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd79536c-bdf8-3d42-8e75-b9209ca07810 | -9.62662 | -62.43391 | 2024-10-12 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f027260-9199-3372-9497-8620d44014d8 | -9.53209 | -62.50072 | 2024-10-12 05:25:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fabb5b9-8887-395b-9712-195dee224237 | -9.52871 | -62.50017 | 2024-10-12 05:25:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aff21b1d-282a-3e2e-bc86-2e459523adc6 | -9.52533 | -62.49962 | 2024-10-12 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51e12c3f-08d0-3eb7-bcf6-129d83bfd39e | -9.46784 | -62.64006 | 2024-10-12 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 405ba8bc-e329-3028-8bb6-22b5ea8cc66a | -10.78316 | -61.50788 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e4bbd3ef-10af-321b-948b-58293e5ec958 | -10.78261 | -61.5114 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b77933b0-d17e-3329-8ce4-816a526df99c | -10.77984 | -61.50735 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39652eaa-e7f1-341c-bd23-8b2b73aa9f93 | -10.77928 | -61.51086 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9aff7da4-a8fc-36e3-b6ac-bcb63fb3876c | -10.77873 | -61.51437 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d12ba3e3-ea2c-3944-a017-14b38f93a297 | -10.77651 | -61.50681 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b310b2a8-62f1-3f83-a8dc-23ea3a3a0ee2 | -10.77541 | -61.51384 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45e9c802-77b9-3601-9c6f-6708a5e425ae | -10.55928 | -62.21358 | 2024-10-12 05:25:00 | NPP-375D | VALE DO PARAÍSO | RONDÔNIA | Brasil | 1101807 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86c5900b-d414-3062-86c4-6025ea6db268 | -10.50322 | -62.97672 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 769daa0a-66cc-3aa3-9a5c-43f87b75eb12 | -10.50261 | -62.9804 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2646d74b-d063-3b04-b446-ce195fdc2d77 | -10.4998 | -62.97621 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57c78fda-f588-37ad-913f-663774c0ff2a | -10.4992 | -62.97987 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70f3f117-5d35-3fbe-8aff-e2ee5def2f68 | -10.49639 | -62.9757 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 033db9dc-4bee-3c03-98f4-b8f969747f47 | -10.49297 | -62.97521 | 2024-10-12 05:25:00 | NPP-375D | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 543e7e26-be3c-3dcf-ba58-da9c2f19220f | -10.47335 | -62.9007 | 2024-10-12 05:25:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 93efce74-f2b8-3508-9b79-196270371838 | -10.46995 | -62.90016 | 2024-10-12 05:25:00 | NPP-375D | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe958ccc-265b-3a88-8f9e-fc01c7ea4ead | -10.33092 | -61.65113 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dfe0276f-b0cf-3579-ac00-ea8fb38213c2 | -10.32482 | -61.64654 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42b3045f-6130-3880-a55f-d253ff604a37 | -10.32426 | -61.65005 | 2024-10-12 05:25:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 498a6082-af40-3024-a53f-b11f1ac866c0 | -10.21344 | -61.89583 | 2024-10-12 05:25:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0041218d-c2f1-334f-b615-f5cc23110d31 | -10.13437 | -62.75151 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9577ec6-fa56-3148-8ca2-75e2d9c1b448 | -10.1304 | -62.75457 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a37a2549-928e-32e8-aa57-0f469c56c409 | -10.12824 | -62.48927 | 2024-10-12 05:25:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa8e5e72-e83e-31a2-9f1f-1662714e64bf | -10.12487 | -62.48872 | 2024-10-12 05:25:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a3a49bdd-cee4-3a8f-91bb-006afc2252f6 | -10.1248 | -62.7461 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9743d4b9-fe7a-3d9a-bea0-861b5c5fd386 | -10.12142 | -62.74549 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41065363-31c0-3663-9dd0-03127f9f2445 | -10.12082 | -62.74918 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c3e0f0d2-6183-3608-8335-d4eaa57bd633 | -10.11743 | -62.74863 | 2024-10-12 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21879485-96f9-3b50-8df4-a84a65a5f3e0 | -11.72097 | -62.60118 | 2024-10-12 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68c566e1-dd95-33f4-a883-c382a760eaaa | -11.71636 | -62.60025 | 2024-10-12 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38ff0beb-dfbd-32b4-8317-f6f59b4af459 | -11.713 | -62.5997 | 2024-10-12 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c6106a49-1afe-3430-8f9f-a20f302b6fc5 | -11.48834 | -62.47854 | 2024-10-12 05:25:00 | NPP-375D | ALVORADA D'OESTE | RONDÔNIA | Brasil | 1100346 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fdd8e5af-622b-3cd2-acb0-326df95881a3 | -10.85701 | -62.32 | 2024-10-12 05:25:00 | NPP-375D | TEIXEIRÓPOLIS | RONDÔNIA | Brasil | 1101559 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 494db674-df74-3c45-bfc7-e5faf2f82af0 | -10.85644 | -62.32354 | 2024-10-12 05:25:00 | NPP-375D | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4922b80-d6c7-3132-b5d7-f80fa0d93984 | -9.42431 | -63.25498 | 2024-10-12 05:25:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 262b374c-9a85-330f-bdcf-0bd03d9d7c28 | -9.31262 | -63.82912 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcfc9130-51ce-382f-b26c-6a521f123160 | -9.31196 | -63.83313 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1b75b8c-cae1-3407-a109-6e6fb44de76b | -9.29457 | -63.21064 | 2024-10-12 05:25:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0baf352-a64e-3e9a-8023-ebf24de39f6b | -9.29227 | -63.53564 | 2024-10-12 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0838f23b-6faa-37eb-8922-b5d2ada7374e | -9.29174 | -63.53648 | 2024-10-12 05:25:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53be9af1-8766-3e20-ad55-32b703202dc0 | -9.28286 | -63.83249 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54299bbb-e302-33d1-8fae-9ed522f150c2 | -9.26222 | -63.82483 | 2024-10-12 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cea923c8-e13d-362c-9f69-c256744c50de | -10.71106 | -64.14537 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c82ef712-7a2d-36b5-9a1d-562eff3defc1 | -10.71039 | -64.14931 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec993259-4e21-338f-b34c-df18072fa632 | -10.7064 | -64.11238 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67da3df4-103c-30e6-b13f-a7a982746a58 | -10.70286 | -64.11179 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb6ceb37-e319-3740-b247-2e9e0800120b | -10.70152 | -64.11996 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2bb175ac-d371-3842-b53f-413a3608ff47 | -10.69996 | -64.10727 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1318a8b-ec7c-3c23-b731-231718169ab5 | -10.69931 | -64.11122 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 150b627b-ed20-39ec-81b9-574f7c1c20b5 | -10.69864 | -64.1153 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25784600-8096-3300-92d2-62760c5280e9 | -10.69796 | -64.11942 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 90e22040-be9f-3c06-8448-f0b4ddc03b76 | -10.69576 | -64.11066 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2793067d-6c1d-325b-9f7c-4bbe4bfe38eb | -10.69509 | -64.11473 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 388bf797-2feb-322c-b9d4-fa267942fddf | -10.69197 | -64.15595 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cc922c0-590a-36b9-9cd6-ddb18368cf19 | -10.64551 | -64.37111 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 087780ea-1aef-3f91-89d5-16eef1efea00 | -10.63942 | -64.43031 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 441a2f43-c8a6-3818-9a9b-f8c59f765e16 | -10.63877 | -64.43422 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 95f81a88-37ed-304a-9e8e-395d03e36189 | -10.63518 | -64.43353 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f6f8d80a-c41a-3035-b6ee-54c82fb4ba3c | -10.6316 | -64.43284 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e966468-85e6-35c1-97a1-d7312e79f483 | -10.63094 | -64.43681 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9bcdc1a-d710-38c3-9df8-3d085de7d4b5 | -10.63022 | -64.44114 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f502d89-bf33-3156-8496-2a01e9394389 | -10.6266 | -64.44067 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc8ddf50-4e9f-3803-a45f-7e3bab9f68b5 | -10.62198 | -64.40168 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e16331d-9cc4-3470-990f-0a87a6266923 | -10.61992 | -64.41402 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5200339a-267b-3fff-9859-6b2fefb08e55 | -10.61911 | -64.3967 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 41220193-6676-39c1-92dc-8bcc8ff93148 | -10.61564 | -64.4175 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66bdf35e-dc6f-3a52-87e7-4655216a8db5 | -10.61248 | -64.36999 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8621b07b-2191-338e-b793-baada62036ca | -10.61207 | -64.41673 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1442415b-b763-3d07-b117-a729aa2ecbcc | -10.61195 | -64.39529 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 57ff2426-fd66-3956-8145-ad4d4a83f2ff | -10.61035 | -63.99405 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3fbd08e-fe74-3949-8db5-899bfa4e18e6 | -10.60836 | -64.39463 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 26b84476-c326-3b02-a537-b9f05d2f05ba | -10.60767 | -64.39878 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53233088-e089-3317-b581-f4bf22a58b8c | -10.60682 | -63.99344 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ba19b83-2a40-3396-858c-8ee7b99f58dd | -10.60478 | -64.39398 | 2024-10-12 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36775918-6bbb-3f45-aa05-73e3bfb03e93 | -10.60394 | -63.98884 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a790ae5-9932-36fd-b255-6cde2a76eb1e | -10.60329 | -63.99284 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2af31863-eefa-3909-9913-30daa8183446 | -10.60042 | -63.98821 | 2024-10-12 05:25:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README134.md)
