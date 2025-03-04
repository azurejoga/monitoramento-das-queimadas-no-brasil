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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 126b7147-65a4-3c75-b9b8-769723e614fe | -22.2064 | -53.42563 | 2025-03-04 04:27:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 990ce001-ad1d-3922-938f-ac836faf12fa | -22.20559 | -53.43016 | 2025-03-04 04:27:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 106dc445-159b-3d40-85e4-4d4ed31e8a3c | -20.83639 | -44.66732 | 2025-03-04 04:27:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fc4f6b43-0a2a-3c76-ade5-f8c2414abcba | -20.74245 | -48.54209 | 2025-03-04 04:27:00 | NOAA-20 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e3790f5-3464-3949-a90e-f7a0d73b4c86 | -20.0902 | -43.99405 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 667ae172-8149-3baf-ad6b-8b04e5ff9b9e | -23.33717 | -46.77282 | 2025-03-04 04:27:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cdfc4d45-07a5-347b-bb3c-85b8443152e3 | -18.14499 | -47.80231 | 2025-03-04 04:27:00 | NOAA-20 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7dfb04a6-b7db-357b-a6ba-71d7d0d965ec | -21.63075 | -48.6811 | 2025-03-04 04:27:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ebcc7a8-ce9b-3a78-9cbe-f41f06fc511c | -20.76804 | -43.15739 | 2025-03-04 04:27:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c10bac36-6d27-3788-8309-9cd9c5d86f4e | -21.6323 | -48.68495 | 2025-03-04 04:27:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50afc01c-f2ca-34d4-9771-ee0f78779008 | -20.09882 | -43.99155 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1d10f21f-824a-3a3b-8e8f-e711df5b1ba4 | -20.79477 | -51.65637 | 2025-03-04 04:27:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| dc5cc4f6-0d58-37be-ac29-02dad01a3ffb | -17.82729 | -45.2593 | 2025-03-04 04:27:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66cf3b4d-f212-3bfd-943c-8f65aa1d06ba | -20.82382 | -48.92268 | 2025-03-04 04:27:00 | NOAA-20 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e165561a-2b55-361d-882a-16030297938e | -21.17967 | -43.97991 | 2025-03-04 04:27:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b9dff99d-2246-3eae-b021-419f2b765e0d | -23.00936 | -50.40662 | 2025-03-04 04:27:00 | NOAA-20 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1dafb4ac-04c3-33cf-a599-51137338cd4b | -20.0943 | -43.99438 | 2025-03-04 04:27:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| eb528fc1-f9a0-30c3-9c08-22a84f608740 | -21.63621 | -48.68174 | 2025-03-04 04:27:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bec3116f-826e-34b5-840c-6f0cd8b6d6a8 | -17.98042 | -47.22219 | 2025-03-04 04:27:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de2dd5f6-cf31-35bd-a7f8-5f6ec015b3af | -21.97314 | -45.72295 | 2025-03-04 04:27:00 | NOAA-20 | SILVIANÓPOLIS | MINAS GERAIS | Brasil | 3167400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7017047e-f1af-399f-b3db-52ab97cc1f30 | -21.88297 | -53.72048 | 2025-03-04 04:27:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f765e55-28cd-38df-b314-ce6b0235830a | -19.96444 | -44.68757 | 2025-03-04 04:27:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99d13459-877d-373b-a42d-e6b10f227092 | -20.76323 | -46.76888 | 2025-03-04 04:27:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d593c657-fa19-36de-bcc8-98bf03899bbd | -21.88212 | -53.71824 | 2025-03-04 04:27:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b29828a0-9486-33fb-951b-00c713948b32 | -20.82772 | -48.91954 | 2025-03-04 04:27:00 | NOAA-20 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7229b015-5ae0-385f-943c-323e8999ac55 | -22.1608 | -47.37053 | 2025-03-04 04:27:00 | NOAA-20 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a6fedc6c-a724-3b47-931c-f6d07ddad37e | -26.25777 | -52.81561 | 2025-03-04 04:29:00 | NOAA-20 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aa91147f-7d4e-34b1-b0f0-66af413292a5 | -29.08084 | -49.60918 | 2025-03-04 04:29:00 | NOAA-20 | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bee5e6e2-5296-32ff-979d-29ca77575d50 | -26.83439 | -51.4626 | 2025-03-04 04:29:00 | NOAA-20 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 81ebf81c-18c9-3f8e-bb5b-486ca1e4a8ef | -27.77131 | -50.69994 | 2025-03-04 04:29:00 | NOAA-20 | CAMPO BELO DO SUL | SANTA CATARINA | Brasil | 4203402 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ffabd93f-66df-30bc-9d1a-109c511f7a70 | -27.48211 | -50.66305 | 2025-03-04 04:29:00 | NOAA-20 | SÃO JOSÉ DO CERRITO | SANTA CATARINA | Brasil | 4216800 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b793aef7-9173-3218-97c2-34677e1a74d4 | -23.50519 | -51.68854 | 2025-03-04 04:29:00 | NOAA-20 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6dc2c667-cbb9-3153-bdda-312a28ddb11a | -26.25708 | -52.81967 | 2025-03-04 04:29:00 | NOAA-20 | VITORINO | PARANÁ | Brasil | 4128708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a3c29e12-18fb-3b84-a80b-3ca7ec51edf4 | -23.98306 | -48.91661 | 2025-03-04 04:29:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3779ddcc-faea-3fe3-852c-77309d9893bd | -24.86395 | -51.99044 | 2025-03-04 04:29:00 | NOAA-20 | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9eb82d80-cca3-34e3-be80-a2bc95f756c0 | -28.62142 | -50.20741 | 2025-03-04 04:29:00 | NOAA-20 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 994d1605-eee4-3baf-b34a-aa1b7eb29248 | -29.00866 | -52.21644 | 2025-03-04 04:29:00 | NOAA-20 | FONTOURA XAVIER | RIO GRANDE DO SUL | Brasil | 4308300 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 68530321-8207-3be0-b924-d0c854ad5d2e | -24.24116 | -50.73949 | 2025-03-04 04:29:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e75b9f53-552e-3035-bba6-20f98d6eb1c6 | -27.54929 | -51.1083 | 2025-03-04 04:29:00 | NOAA-20 | ABDON BATISTA | SANTA CATARINA | Brasil | 4200051 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff2d104e-a75e-3616-9369-a4d8ca75adff | -23.50455 | -51.69238 | 2025-03-04 04:29:00 | NOAA-20 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 41704c2b-38e1-3d66-b879-b96fbb32e846 | -26.42096 | -53.09585 | 2025-03-04 04:29:00 | NOAA-20 | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79a7839a-5805-3dbd-89a1-81c78d80bc14 | -29.07804 | -49.60992 | 2025-03-04 04:29:00 | NOAA-20 | SOMBRIO | SANTA CATARINA | Brasil | 4217709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b842450a-7f47-340a-9062-771fd5a30953 | -25.33988 | -49.21703 | 2025-03-04 04:29:00 | NOAA-20 | COLOMBO | PARANÁ | Brasil | 4105805 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 60f84e71-5fb1-3be2-aa7d-dd1c92eb400b | -25.12776 | -52.3458 | 2025-03-04 04:29:00 | NOAA-20 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7a36b4b7-cc2e-3202-b149-4e6022370a09 | -27.2538 | -51.32394 | 2025-03-04 04:29:00 | NOAA-20 | HERVAL D'OESTE | SANTA CATARINA | Brasil | 4206702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 28fd8089-dd33-31ce-89f5-c3f51fc5f054 | -25.1298 | -52.35438 | 2025-03-04 04:29:00 | NOAA-20 | MARQUINHO | PARANÁ | Brasil | 4115457 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b24ea1df-46b0-3cd9-b605-3f38cce50761 | -26.83377 | -51.46646 | 2025-03-04 04:29:00 | NOAA-20 | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f7995b0a-d60d-31b7-8cee-7c73578a80e2 | -29.66806 | -49.97785 | 2025-03-04 04:31:00 | NOAA-20 | CAPÃO DA CANOA | RIO GRANDE DO SUL | Brasil | 4304630 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| a5a69844-92f6-30d4-bac2-86eb324bf3b0 | -30.4292 | -53.5167 | 2025-03-04 04:31:00 | NOAA-20 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 74206249-4b64-32b0-9a66-d33d707421e7 | 2.35401 | -61.04797 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2e9e381e-0d4d-3c1f-96a5-8d6ebb58e240 | 2.36297 | -61.05585 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 899c48ac-460f-3630-8426-b84039bef675 | 3.04304 | -60.11933 | 2025-03-04 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40a41f6e-877a-33b3-9e4e-17d85356d40c | 3.42731 | -60.71525 | 2025-03-04 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d75f951-c186-318b-9514-640477efeb25 | 2.20915 | -60.54775 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8aa7e75d-65c4-3415-b73b-750461ea7546 | 3.05666 | -60.08739 | 2025-03-04 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5597c66-68ab-37b7-bf94-7da1c0d33362 | 1.9356 | -60.40259 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2cb783e-0b30-3981-a575-06620ae339a4 | 3.5017 | -60.18008 | 2025-03-04 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85ccb99e-342f-36fe-bb8e-3759c57a2ea2 | 3.53863 | -60.10499 | 2025-03-04 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8e0b05e-5264-36bf-bcba-d1081eb638ad | 1.76302 | -60.22848 | 2025-03-04 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cc5331cd-5c1b-3f18-9944-a105f8e2f3cf | 1.89023 | -60.85881 | 2025-03-04 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85759268-6972-32ac-a251-4faef2244e39 | 2.35778 | -61.04735 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0542463c-e45e-3d7e-b938-f771c3b5acf0 | 2.61897 | -60.14044 | 2025-03-04 05:14:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38af28be-cf41-3a7e-aeb0-d969df69caf7 | 2.35849 | -61.05193 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9f91c1aa-a0f8-383e-a9f0-ae1041239328 | 1.76724 | -60.23206 | 2025-03-04 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 51226cce-bdc8-3494-a340-1925734750d6 | 1.79156 | -60.27052 | 2025-03-04 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8e7b866-e8ad-3183-a41d-28d4390a2bd0 | 2.35708 | -61.04284 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fad1d4bb-761c-3787-8b06-f9debea6a0f2 | 2.00487 | -60.55864 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da073da5-221e-3551-8c58-ab0411687d47 | 3.42789 | -60.71259 | 2025-03-04 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 33de75bd-c73f-31c1-a713-9a3fd1253a5b | 2.36227 | -61.05134 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd22d734-71b5-30f5-bdf8-c14aff6e3e22 | 2.2661 | -60.25413 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4f89f8d-ee8f-3662-ae83-ebd38e6dd46d | 2.35472 | -61.05256 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 66012f59-2632-3e4f-a822-6e0c5d8fcfa4 | 2.00048 | -61.14408 | 2025-03-04 05:14:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b0baa372-d705-30d2-8eb7-5a6115ffb8e8 | 2.36156 | -61.04678 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9d590df-a1c2-33b2-ba6b-7d3dfcbd1d08 | 1.93922 | -60.40197 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52ff1a5e-1f84-3998-acd6-17598de58eb7 | 3.54161 | -60.10022 | 2025-03-04 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb455d19-a146-3860-b23d-444c9321a050 | 3.54459 | -60.09545 | 2025-03-04 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2f0ffaf-d972-3006-8db1-01de3d709a72 | 2.3396 | -61.05486 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 708eaf36-05cc-3583-806f-2b1d3b2b8dd6 | 1.93792 | -60.39365 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72f3c8aa-b00e-3a58-a364-d6b501da5338 | 1.76365 | -60.2326 | 2025-03-04 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 99f50470-b79e-3fb8-9bef-df7dc82afd3e | 2.34337 | -61.05423 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 552f25d1-1e30-3681-8468-a8455a53bbd9 | 1.76428 | -60.23671 | 2025-03-04 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2dce6bb7-dd50-328e-9439-a50aea8a3ff5 | 2.34784 | -61.05816 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be511481-f58b-3aad-b5f1-f389df864528 | 2.16627 | -61.83635 | 2025-03-04 05:14:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9169f3f0-fb26-32b4-b2d0-061757e00721 | 3.51975 | -61.57248 | 2025-03-04 05:14:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd4cd1a4-7597-378c-9605-b6ecdf906125 | 1.7958 | -60.27412 | 2025-03-04 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c46fb40-1e3c-3255-9b36-fb801808dbaf | 2.82305 | -60.49363 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06e4f746-261a-3034-8613-4117f27de6a5 | 2.33869 | -60.51218 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea2f5724-369e-3ddb-8e27-5ef0ed8a8aa2 | 2.27033 | -60.25767 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 38b1db63-3244-3a5e-a7d9-306d1fc885aa | 3.41814 | -60.73055 | 2025-03-04 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41356e41-86d9-31b6-bdf6-6a1ef035419a | 2.09831 | -61.81538 | 2025-03-04 05:14:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65478b49-394c-33be-bcac-3d2ce5e78bb1 | 2.76119 | -61.42164 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b82dd5cf-1226-3fe9-bdfc-cf0761881243 | 2.74687 | -60.72874 | 2025-03-04 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 535584d4-e530-3e4a-967c-c081ac29cb5f | 2.35163 | -61.05764 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| df851ee6-fdbe-397a-96df-c026c9de6928 | 2.74756 | -60.7332 | 2025-03-04 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26702c26-a6b8-39aa-acd0-0b90bcdc67d0 | 1.93495 | -60.39841 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c375d997-0bb0-3e38-9090-a27b62f2a0d8 | 1.85619 | -60.29519 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f04d3289-1533-388c-a8d3-d19b152a806b | 1.76006 | -60.23312 | 2025-03-04 05:14:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 538f79ba-b8b0-3950-913c-51c92b721bb1 | 3.41743 | -60.726 | 2025-03-04 05:14:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ef9a3c38-9a66-3644-88d3-2ffec287cb80 | 2.35302 | -61.06665 | 2025-03-04 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8a249db-5584-38b2-9fe3-b614b5cca340 | 1.94088 | -60.38885 | 2025-03-04 05:14:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README7.md)
