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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5f7bd33-b186-3f2f-bb0b-fc22591a51a0 | -12.95181 | -45.94109 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a38cdc70-ec20-37f0-a352-c1201d41df49 | -7.34453 | -60.60051 | 2026-08-31 04:59:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eaf98e66-53c8-38d3-8e69-160179b6409f | -13.64333 | -51.84211 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 844141c7-1f77-3541-9f30-c0f370a45b46 | -14.41195 | -52.5253 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 32b63b79-30d6-3764-bfd7-a86746dfdf7e | -8.55795 | -54.7142 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31a98d4b-bd10-39d7-b21b-cd61c7f39b94 | -9.19354 | -51.56198 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c42fe3ed-248c-3e96-a3b4-5c02ab35a661 | -7.69434 | -63.33289 | 2026-08-31 04:59:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a699a53-39a9-3e22-8f99-bced3bf6529d | -9.58417 | -47.6128 | 2026-08-31 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| e085a7d2-b5b7-35fe-b786-e60922de9bc9 | -15.66489 | -45.91181 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9abeb4c8-41bc-3481-a6cd-8d2e04a71497 | -9.35876 | -60.30228 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa2033b0-bb2b-3dbc-8c4a-8b7f3e476920 | -9.06682 | -60.49056 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38b7d647-bbe1-3470-b4d7-fc4f14b6cec3 | -11.3778 | -45.2155 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd5ce716-c2cc-3983-9aef-627c1df99f90 | -14.66131 | -53.57509 | 2026-08-31 04:59:00 | NOAA-21 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7134d3c-48ff-3227-93ea-367d9223afd6 | -10.15241 | -45.69812 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c19d52f6-7f37-3598-837d-b38d44e82f39 | -10.16016 | -45.73746 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7b44b75-0642-3b32-9d2c-6fff3f3429e6 | -12.17801 | -50.52729 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4144f241-2915-33a4-9f99-73fa005ba4b7 | -11.36405 | -45.21564 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a43bb5ca-f2aa-3a1d-b634-da24232a8e01 | -10.74818 | -54.03667 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7e726b26-eaf8-303c-9d6a-42b97be17cf4 | -8.6147 | -54.71951 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c25ba034-3de8-3912-a3ca-e083804b73d6 | -14.43331 | -52.52617 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6254cab7-6e49-3fa1-904d-21aa59cc1f7f | -11.2197 | -45.09725 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0f9f050-1f40-31a9-a37e-356c3a125502 | -13.57048 | -55.15781 | 2026-08-31 04:59:00 | NOAA-21 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4165225-9992-37e6-adbe-f77a86d0079e | -13.19363 | -44.07489 | 2026-08-31 04:59:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea293fb2-2d53-3362-bec2-906b72e9e30a | -9.84018 | -64.98201 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 482a22db-c9b0-32eb-9909-76831581382b | -7.44624 | -61.42724 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1ab42ce-5cc3-31f0-8072-37c78ab9e4e6 | -9.96493 | -46.30956 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| def103e1-1e7c-36a1-95d6-b2a487a6c756 | -9.01402 | -65.4003 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd87b54e-c2d3-3354-b21a-42745fa0280c | -7.58661 | -61.3517 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8237425e-9564-3bc4-875a-a8baaa0f061e | -11.15638 | -50.5607 | 2026-08-31 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0f0a007-ba04-376b-a703-e0a5c9968ac2 | -9.96977 | -46.31301 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0bc2f71-f453-3d24-aba7-873686f7023b | -9.20691 | -51.57261 | 2026-08-31 04:59:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8c55b57-139a-379a-9937-42bfaf7e1587 | -9.8502 | -64.98746 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0882c94-67d0-398f-92c9-428fb4b557bc | -9.17328 | -59.63385 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d7f3ffc-f77f-3d39-96b5-48476b446858 | -13.42049 | -51.3814 | 2026-08-31 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47466be8-9a68-361b-883f-24b3486cf23d | -15.66408 | -45.92805 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13cf34ed-2cca-3c50-b126-8317d1bc7343 | -11.20812 | -43.38041 | 2026-08-31 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 59acddf9-0983-3686-a914-38d2b45849b0 | -14.43637 | -52.53129 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8546b84-ad70-3e25-807e-6ea750ef24c3 | -11.08308 | -51.52266 | 2026-08-31 04:59:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a39875f6-b82e-3669-89d2-b2a9a229c52e | -14.59895 | -54.12206 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 05225bc6-be81-37d4-8af0-a8fa54e96ca1 | -11.35681 | -45.22748 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6fe3bbf6-6d3b-3aaa-a9fe-3a7f403a2537 | -14.19779 | -46.56538 | 2026-08-31 04:59:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55071f70-1ab0-3d1a-8fe3-da4b657fa682 | -9.22674 | -59.57907 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef31c00c-6ea5-37f6-85bc-263c97449c36 | -14.30245 | -52.90193 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0891ac36-31d8-312c-98d5-5ded87bf7643 | -14.58683 | -53.08387 | 2026-08-31 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8ce2cfc-81b0-3dbc-a80c-bbe6e07cdc39 | -15.66901 | -45.92725 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7de1e374-df24-39f3-8860-f24e5e14d676 | -10.76778 | -54.04345 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36f04799-0c0e-311d-a44a-e9d5e1c2d242 | -14.17568 | -52.87573 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22eaadf4-f564-3ec2-9245-4b763444a241 | -9.80759 | -46.45174 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c02adf6b-41c6-379e-ad41-72037680d13c | -15.66449 | -45.92405 | 2026-08-31 04:59:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15d11c50-4ad6-320e-8212-d45d1de592b2 | -14.23723 | -52.85852 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0ddab275-094b-317d-addb-7d4dbf8df663 | -10.31447 | -58.08932 | 2026-08-31 04:59:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 09c25df6-e96b-30ad-b79b-41bd841d32d3 | -11.37585 | -45.21402 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cf1d1222-8305-3770-9357-2ba2dfd3f9f5 | -11.93349 | -45.05347 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53d8f489-cac5-3d06-9766-826351fdf001 | -15.20404 | -46.23038 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f67c236f-3e77-3a0f-a096-7ef2f0597adc | -8.6591 | -54.76277 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20a5e502-2955-38aa-9d39-12cf63319a39 | -9.1797 | -59.6194 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 140773c3-cce0-3099-93fc-1d6f3a2e2974 | -11.93361 | -45.05287 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b375a81-40ac-3bb1-9010-32e8fbb75b88 | -12.11351 | -45.03002 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d483386d-9543-3802-b552-a34981e94f40 | -14.22395 | -52.84795 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0bcc6f7-390e-3f68-99c7-09444b79ceff | -9.17733 | -59.63262 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3d5f61f0-d65b-3c30-bb19-3540cec17e9b | -14.46662 | -52.19927 | 2026-08-31 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 098c77bc-f11b-361d-980f-e553c81a63ea | -9.80325 | -46.44485 | 2026-08-31 04:59:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77e032ef-9293-3382-8020-4945de817a85 | -10.56758 | -50.36677 | 2026-08-31 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d6e6e4d-7234-3793-88b7-d7f025a18d29 | -14.4259 | -52.57982 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80a2e331-ce7b-3d57-8628-e58091f64277 | -9.14344 | -61.09812 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c1a821f2-3982-31ac-962d-719dfd92217b | -14.16198 | -52.78351 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d63e3706-6097-3013-8416-86d27acd569c | -9.05293 | -65.41903 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c9ac633-2c78-32e6-95ae-8682d857e5cb | -11.35935 | -45.20669 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14fe098e-6824-36e2-9751-21448f4f92e6 | -9.72276 | -65.0023 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65513a27-9473-3b09-b6be-e3a908e85a6b | -14.39833 | -52.54153 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cbb2af50-34d6-3964-b119-004547896057 | -13.64404 | -51.83709 | 2026-08-31 04:59:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39794747-9959-3706-88e3-0bffd2ed54f9 | -10.154 | -45.74257 | 2026-08-31 04:59:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c06b24f-90db-3ddb-adac-43b5c310d8a1 | -15.06576 | -48.00687 | 2026-08-31 04:59:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1959cff9-f59d-3195-99ab-f9eed295e8fd | -8.58333 | -66.96962 | 2026-08-31 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e5a7be4-9f23-3fbf-bab0-6e8867cd92a5 | -10.7636 | -50.85426 | 2026-08-31 04:59:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b1189a0-2def-3255-8682-2e143ff12042 | -10.84119 | -48.3385 | 2026-08-31 04:59:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c883d1df-341e-3cbe-a52e-1734666453f1 | -8.30597 | -54.67054 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71e56265-f0d4-30f9-b866-9db6b493cea1 | -11.32861 | -45.17295 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc057a9a-bf4d-3521-b2bd-97693f1cf316 | -11.49797 | -46.93373 | 2026-08-31 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f953c248-ddb4-3e8c-8560-419f103db20c | -12.78393 | -46.45795 | 2026-08-31 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ab8ba3ca-147c-33cd-91c1-322d4f11359d | -9.13959 | -60.52602 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbc3a576-cfe1-34d1-ba71-bbe459a55101 | -10.76723 | -54.04705 | 2026-08-31 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c619e80-ce25-37a0-8f17-65d9ab32a5d1 | -7.58105 | -61.34664 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac90975b-a03e-3698-9a48-ca14fd75e470 | -8.6165 | -54.77315 | 2026-08-31 04:59:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8d96832-2f44-3ff2-ac92-2bb950ccd5c3 | -10.48238 | -59.60849 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0b8dcf8-62d1-3aa2-85b7-d0d9247e9b4f | -14.29944 | -52.89711 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8557963d-7751-3c45-98c3-ab95777b7f88 | -13.05776 | -45.18137 | 2026-08-31 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa82820e-c86a-382b-a9bd-2bea1d1aa466 | -9.85607 | -64.98877 | 2026-08-31 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f381d010-6d8d-389a-90ea-ab99dd9cebc9 | -9.91152 | -60.15146 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a414eab-eecb-3a14-82f0-04b4e95b45a2 | -15.19845 | -46.22945 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 660fae22-9c6a-3558-9457-2af5f622a550 | -10.41861 | -57.22594 | 2026-08-31 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e12edfb1-9fab-3e85-ba3a-8bbb836f9c8e | -14.58517 | -54.09627 | 2026-08-31 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2eb6371-5a44-3b58-859d-f9ef746001cd | -7.3993 | -60.57989 | 2026-08-31 04:59:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52a75f0b-9ceb-36f2-9ce6-c3a4784e013e | -9.20245 | -59.58011 | 2026-08-31 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b8c86bf-538d-3014-b2ad-52d4a762b998 | -11.37311 | -45.20597 | 2026-08-31 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c0f5f04-d12c-39db-b219-e57546cbd0da | -8.95128 | -62.36345 | 2026-08-31 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| affc2f7a-92b0-3609-b725-da238db57773 | -9.58544 | -47.61383 | 2026-08-31 04:59:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b6309ec1-67a6-3f2f-899b-7a9edbb97bc4 | -9.79736 | -60.18266 | 2026-08-31 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b9aaba6-b905-3134-8282-7f268fb20839 | -7.79155 | -61.58183 | 2026-08-31 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 605929ff-7807-37a6-a6f7-dd4ed40306ac | -14.30184 | -52.90619 | 2026-08-31 04:59:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README51.md)
