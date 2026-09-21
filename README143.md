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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49f4beb7-1ceb-3236-ac3a-69ac231a6554 | -10.6189 | -50.2466 | 2026-09-21 15:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 33373cb0-dfa6-3541-9794-74c9fe895fbb | -4.2964 | -56.2596 | 2026-09-21 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0d897664-777c-3b83-93be-0a6334420dce | -8.1871 | -54.7824 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 6c1ca2a6-dbc5-33a1-a8cb-126f15bb4ad0 | -9.0866 | -61.0287 | 2026-09-21 15:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 04a17cde-2e39-39c2-b831-c1196374c8d0 | -11.0223 | -54.1379 | 2026-09-21 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 58d09f96-cb3d-30e6-9438-58b21a3e0b3b | -7.3291 | -55.1955 | 2026-09-21 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3bec072a-d460-36a3-b100-3081061ee19e | -11.0412 | -54.1362 | 2026-09-21 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 344.2 |
| 79876e6e-43d4-3487-b424-30786d1b57f7 | -9.5594 | -66.0359 | 2026-09-21 15:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 134.5 |
| b55a4260-a678-3938-a0ce-930eadfbcec6 | -5.2546 | -55.9303 | 2026-09-21 15:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 115912ab-6e04-302e-b071-ca6d0b7dd089 | -10.2635 | -49.984 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 2c376dc4-f2d0-3f42-8100-c6990f1cd548 | -10.279 | -50.2391 | 2026-09-21 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 010f5786-c548-3a86-84a8-895d537f20af | -7.5889 | -57.6757 | 2026-09-21 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 250.3 |
| 5fba1661-b401-3bdd-aad0-d02dbd8a7993 | -9.3986 | -48.3213 | 2026-09-21 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 131.9 |
| 1f86c374-e118-341f-8a76-7694c5d720f9 | -6.5569 | -45.566 | 2026-09-21 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 236.6 |
| 1ab55745-ae6d-3a40-a97d-865888c319af | -11.8559 | -49.979 | 2026-09-21 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 1bb4aeb7-6af7-3c88-881a-aa7cca212512 | -9.8686 | -48.447 | 2026-09-21 15:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| bbf9391d-8c98-3100-900f-b90453294d16 | -6.9223 | -42.9323 | 2026-09-21 15:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 235.2 |
| 2322b7dd-d5ba-3008-8081-991fff94cf94 | -10.8921 | -53.9857 | 2026-09-21 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 5abf550e-04c4-329e-80bc-77e1afec1605 | -6.5759 | -45.5419 | 2026-09-21 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 187.9 |
| a53fe6a6-38a6-38bf-9d5a-50e90a880b4e | -8.2388 | -55.2616 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 505.0 |
| 0956437a-f218-376a-88f8-ba0cd8200efb | -6.2034 | -45.3453 | 2026-09-21 15:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 91827fd2-d905-39ef-a4c7-7dbd698d3462 | -11.0598 | -54.155 | 2026-09-21 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 27344d70-81af-3a1d-8b69-f1f2d2f941d3 | -3.3455 | -61.2908 | 2026-09-21 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f1d78bab-7ce4-3879-8992-2cfd7468114a | -6.6413 | -52.9686 | 2026-09-21 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 18fd0b2e-c53f-388a-ad93-abc8e0d12d4f | -7.5703 | -57.6962 | 2026-09-21 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 257.5 |
| 97d33cef-6393-3b7b-b4e2-6d97f0e8a7b0 | 1.5469 | -55.8255 | 2026-09-21 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 57a5a802-6500-3bab-a5f7-28c6a1bb2438 | -8.3764 | -47.2802 | 2026-09-21 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 0f0e58cb-6767-3cb5-ae0a-cc73cb085ab7 | -11.875 | -49.9767 | 2026-09-21 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1a1227ea-6c49-3ace-9fa7-28b99b885747 | -7.252 | -55.5794 | 2026-09-21 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| e3cc112b-d689-3cf9-83d1-2271fe04d5cc | -10.0898 | -50.2795 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 828acfbc-ba24-3518-8119-364a71d37b89 | -3.3505 | -59.4082 | 2026-09-21 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 9fd3a602-e459-3c52-b722-501fc62edee2 | -12.9091 | -50.9672 | 2026-09-21 15:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| b792531a-b28b-3aa0-9e97-5016d486bf5c | -5.6406 | -43.4153 | 2026-09-21 15:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 5edbb909-8d9f-387a-a398-649a6811a7cb | -5.8412 | -53.4799 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| bdab5e05-e4ef-3534-b391-505e77d456e9 | -3.1698 | -58.5859 | 2026-09-21 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 88a57445-35e8-3218-9479-57f8053bd8b5 | -3.3455 | -61.2908 | 2026-09-21 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| bdd9507d-935e-33fe-8abf-3f3cd60864ee | -10.279 | -50.2391 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f0c1ed33-d0f1-3ee4-bb33-0c7f8d9ed369 | -6.8264 | -55.5222 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 86e99a95-6fa0-3ab4-82c2-ec1be84eccab | -10.4105 | -50.2897 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 3f72750c-0e9b-3a6b-9986-6e33f51e9b4f | -8.1874 | -54.742 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 9e941ad0-4b4f-305a-81fd-3886d4a2f3dc | -12.0454 | -50.0424 | 2026-09-21 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f760d904-f49d-3669-ae22-fc4ca3555ddd | -6.1653 | -47.5052 | 2026-09-21 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 0cc9c263-bf29-33a5-a174-2bb60daae25e | -6.8466 | -55.2817 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 189.8 |
| 19e8bac4-1c6f-325d-afa0-9d894e67c61d | -6.2948 | -47.6274 | 2026-09-21 15:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 2fd63b75-2c67-3704-8f36-647fae081b18 | -10.7463 | -50.6172 | 2026-09-21 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 61184e5f-2b01-3637-9d92-15ed3d5378e6 | -10.9361 | -50.5759 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 7a612208-9b14-3d3b-97e4-c71cb8d6fc21 | -8.6169 | -54.6328 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 11217464-d822-33c4-a6b4-6005b6216a7e | -11.0412 | -54.1362 | 2026-09-21 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 284.3 |
| 6a701f85-aae8-3944-83dd-0d6f5588841c | -11.0223 | -54.1379 | 2026-09-21 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 9f5478d2-b9b9-33ec-b022-5e4094963633 | -9.0682 | -61.0104 | 2026-09-21 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| ac8282d2-e93f-3d41-93dc-5252e71ba847 | -9.8683 | -48.4689 | 2026-09-21 15:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 8181f832-c96c-3c00-a103-fd0c577fa0c5 | -8.1686 | -54.7634 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| ec1d595e-84ec-30cf-8dc8-862e6235c6e3 | 1.2055 | -50.9974 | 2026-09-21 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 78e797fc-851c-369c-a73f-5f03a122e14e | -8.1876 | -54.7219 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 92d6d50f-70f6-3b99-93bc-1f7f3bb470c0 | -10.809 | -50.1836 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 059347d0-70f3-3352-82f6-cd026f166bdc | -8.2388 | -55.2616 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 399.8 |
| 9c277084-d9a2-3096-aeca-e0ad1490bc78 | -9.5408 | -66.0365 | 2026-09-21 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| ddbc07aa-7797-35a9-94c0-a7082c4b85ed | -11.3809 | -44.0788 | 2026-09-21 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 218.6 |
| 7b9252a2-51e0-309e-a0da-704115ba1699 | -10.4102 | -50.311 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 9b1a9c30-b8db-3762-97a7-4bed631a6b97 | -10.336 | -50.2119 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 127.6 |
| 22a30565-cd0e-39c4-ad68-57b50fa6f63b | -6.8263 | -55.5421 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 34035a32-5e87-39b5-bcdf-f396896750c5 | -6.2582 | -41.6858 | 2026-09-21 15:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 066d069d-a529-3edb-ab6f-654c2b1e957d | -10.2635 | -49.984 | 2026-09-21 15:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 4483b31a-4d2c-3127-9f33-39c2da5087be | -6.5444 | -44.9327 | 2026-09-21 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 050e021b-c574-3dff-88c1-f74e9d18dc35 | -6.7369 | -55.0874 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 83d45f84-07b4-3112-b44c-cacbff805f34 | -6.5761 | -45.5194 | 2026-09-21 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3ee5d9e5-472e-361c-97fd-e2f120845850 | -9.1056 | -60.9703 | 2026-09-21 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 6ada186a-e414-3886-a4a0-0c05ba7de13b | -3.3359 | -58.1191 | 2026-09-21 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 36b2612f-6860-3b32-9682-a5c5f3964d6a | -7.252 | -55.5794 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| ed6c8f68-8759-3be1-a34f-c6d226ff55d5 | -6.583 | -58.9658 | 2026-09-21 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 8752a43a-d9ac-35ab-9b6f-7a4170365541 | -11.8559 | -49.979 | 2026-09-21 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.5 |
| d2d7640c-82e1-3d32-b98a-a1c32bbbd798 | -3.6448 | -58.8839 | 2026-09-21 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2dcb460c-8153-3a98-b8f0-b812ddf23f74 | -3.478 | -59.597 | 2026-09-21 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 447e245d-f86b-392a-a1d5-49c513d2f6fd | -8.5982 | -54.6341 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 747357f7-4af8-3ddb-b22c-274b6d050b7e | -6.6761 | -50.9381 | 2026-09-21 15:40:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| cf85a5c6-d617-3e4a-a85f-9b9e5450bf00 | -7.3291 | -55.1955 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| b90bc367-204b-343e-b363-05d848282518 | -9.5594 | -66.0359 | 2026-09-21 15:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 140.3 |
| ffab9cff-4e32-36cd-83fb-3021a2f6d3b4 | -10.7715 | -46.3001 | 2026-09-21 15:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 4f25af9d-1244-3f9f-bfb9-5e5c4ce5ff5f | -10.8659 | -50.1775 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 02ed6e76-52bb-3adf-a6b5-1847be43f2e0 | -6.392 | -45.1948 | 2026-09-21 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 157fabe2-fb93-3304-b86e-0d4e3a389d0b | -7.9152 | -72.9324 | 2026-09-21 15:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 42.0 |
| b0d2702a-91fb-3305-b42b-4e0c05321241 | -6.5449 | -44.8871 | 2026-09-21 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| d8360931-83bc-3ba4-b8d8-709c53091bbc | -3.5893 | -59.0773 | 2026-09-21 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 79dc0da6-1bbb-31f5-b8c1-13dc102ac872 | 1.2239 | -50.9972 | 2026-09-21 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 4ad6746a-bf3a-3603-835b-e474430e1509 | 1.2424 | -50.997 | 2026-09-21 15:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 776d17ae-352a-3a62-8973-211a5fc78beb | -12.3206 | -50.7394 | 2026-09-21 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 5f56d902-564c-3fbb-8f31-6c5f891b23a1 | -10.6881 | -50.7297 | 2026-09-21 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 6a6909f1-a348-3277-b8fc-21181325647a | -10.8093 | -50.1621 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 5d90f221-d7b7-383a-8337-28da220d486d | -8.0894 | -55.331 | 2026-09-21 15:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| a414930c-241f-3144-b852-fa54562ce9db | -2.9525 | -57.72 | 2026-09-21 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 7c4be713-09d7-3db8-ba12-c148aa8b80f8 | -3.753 | -59.419 | 2026-09-21 15:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| cd5ff389-a6f8-3f8b-8aa7-479dd2b1ceae | -11.875 | -49.9767 | 2026-09-21 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 5f5fbb14-460c-3f20-9ae6-8c695ab57538 | -3.3638 | -61.3093 | 2026-09-21 15:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 369d3659-032b-3e71-b254-9d6865c50b44 | -3.6449 | -58.8647 | 2026-09-21 15:40:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8ab44fd3-c65f-306d-9bc3-92da991e1868 | -11.3996 | -44.0995 | 2026-09-21 15:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 184.5 |
| 9455d3ae-8f28-3624-9345-4e367882458f | -3.3504 | -59.4274 | 2026-09-21 15:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 7afacb30-c1ca-3e5e-a132-44a06ded3bb1 | -10.8096 | -50.1407 | 2026-09-21 15:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 1beb269e-a2e5-31de-8f2f-aee66d86b018 | -6.4228 | -55.0233 | 2026-09-21 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b5b2e346-a792-3b77-9241-67a1ad7b525f | -10.7652 | -50.6153 | 2026-09-21 15:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.7 |
| a4122601-b017-3c33-a6df-01a43a0608b0 | -2.9526 | -57.7006 | 2026-09-21 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |


[Clique aqui para ver as próximas entradas](README144.md)
