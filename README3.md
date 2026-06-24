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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a001a16c-6a58-3811-91b0-e9a2dd420b5d | -12.776 | -44.4458 | 2026-06-24 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 34df10da-0be5-3c44-a7eb-c5e9fe357f6c | -6.3703 | -43.5898 | 2026-06-24 00:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| ca0b501d-8ca2-34c4-b46f-6a0d7c68f7cb | -12.7764 | -44.4223 | 2026-06-24 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 2e60df49-daa0-3885-82e2-3b0a38d8b0fd | -6.5924 | -43.8957 | 2026-06-24 00:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 08b55e11-af82-38ee-b9de-12de9a653c3e | -8.6181 | -45.9854 | 2026-06-24 00:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| e0565975-6817-3533-8098-a5181645203a | -12.776 | -44.4458 | 2026-06-24 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| a4bcf134-47a1-3260-a814-30aa8f201ebc | -13.0827 | -53.3524 | 2026-06-24 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 045079bb-b455-3e28-af9e-fe62c888d65f | -13.0635 | -53.3546 | 2026-06-24 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 170.2 |
| f1282b8b-1eab-335d-a495-a351514ca1b0 | -12.7953 | -44.4426 | 2026-06-24 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| e9478f58-b1e0-36c5-a6fe-891b5aa5478f | -9.457 | -40.3889 | 2026-06-24 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 170.6 |
| ba8a9488-f450-3f51-8c10-4b25235799e7 | -6.5924 | -43.8957 | 2026-06-24 00:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 22385e59-3a4c-3dd9-aca9-adfc7208e8ac | -13.0827 | -53.3524 | 2026-06-24 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| a3fcc38a-bb48-343e-af2b-ebe7807163ec | -12.776 | -44.4458 | 2026-06-24 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ad945f55-e3de-324f-9f09-8ad0a3b5ca7f | -6.3703 | -43.5898 | 2026-06-24 00:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f7582290-c080-3e6d-9161-dd55b64bb46b | -9.4574 | -40.3641 | 2026-06-24 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 197.7 |
| 1302811f-6bd5-3360-8d0d-535d034d8dfe | -12.7764 | -44.4223 | 2026-06-24 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 275e68d6-398f-32ee-a5bd-8dec2e42bc3a | -12.7953 | -44.4426 | 2026-06-24 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| b73a9472-aae3-3d33-b18d-9f8209091056 | -13.0635 | -53.3546 | 2026-06-24 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 0df1abc4-c1b4-3147-b8bb-5641e9ded814 | -13.0638 | -53.3337 | 2026-06-24 00:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 6c293eec-1d3b-38cf-b831-3c5301206efb | -12.7773 | -44.444801 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4b2182de-e6a3-3db9-b3b9-151398597253 | -6.5853 | -43.901402 | 2026-06-24 00:43:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6913bd0e-2cbf-31f9-a226-a29c6d08722a | -9.459 | -49.829601 | 2026-06-24 00:43:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14529f67-3975-3bf5-9255-75655569b7b0 | -12.7291 | -49.082001 | 2026-06-24 00:43:00 | METOP-C | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 29496f58-f742-3dd4-996d-f7f8ebbddaea | -6.8465 | -47.857899 | 2026-06-24 00:43:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7729d75e-aa7d-395c-87b4-9824dee4a595 | -8.6802 | -47.848499 | 2026-06-24 00:43:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2feb492b-38f3-3561-a4ee-5334324e6bf7 | -11.915 | -44.168098 | 2026-06-24 00:43:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d85da0dc-9455-326c-831a-8e2af4321df9 | -13.0631 | -53.355202 | 2026-06-24 00:43:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44c68269-e7c8-3084-8bc3-2e2f9820574e | -13.0654 | -53.3666 | 2026-06-24 00:43:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab154892-99b2-3c3b-b02d-ab26a1f279b8 | -11.5492 | -48.269199 | 2026-06-24 00:43:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e39523c-00f0-35c2-87fd-c6ff9bb25df5 | -6.3101 | -44.647499 | 2026-06-24 00:43:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f83eb47a-544a-396b-b970-3d319caaff47 | -7.2969 | -46.2467 | 2026-06-24 00:43:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec236fa1-4e4f-329e-b9aa-81308a147642 | -6.8449 | -47.895802 | 2026-06-24 00:43:00 | METOP-C | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01eb927d-bd39-3543-a4a1-fb85aa4dcf30 | -9.3821 | -41.221199 | 2026-06-24 00:43:00 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| c82765d2-d0b0-3646-a6f6-ce1c86cffc2d | -7.9581 | -43.905701 | 2026-06-24 00:43:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 26e66226-cc9c-3b57-94f1-635ca125cee4 | -10.6953 | -49.6059 | 2026-06-24 00:43:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6d8f8e7-f3cc-3c4a-95e7-6e3d8a2e49d2 | -12.8485 | -44.353699 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b4e4108a-a9b8-3f53-bcb7-74abf87ffdda | -3.8701 | -42.965199 | 2026-06-24 00:43:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33f26d3a-f9ea-31a6-8a06-b4efc8f72c2f | -6.2584 | -49.883701 | 2026-06-24 00:43:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d671feee-6dfe-361f-844c-990be8b5d916 | -6.3695 | -43.6036 | 2026-06-24 00:43:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9319e731-351b-35bf-9f80-6aae3c765e23 | -11.2382 | -43.337399 | 2026-06-24 00:43:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1ed595a6-4a48-3236-930b-a66648802494 | -10.3829 | -56.7188 | 2026-06-24 00:43:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 067df213-685e-3b56-b6b3-519cfc10128a | -13.0752 | -53.364498 | 2026-06-24 00:43:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1747b1-6eee-3d2f-9bb1-924f7e02ee00 | -12.8388 | -44.356098 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76faa418-773d-36db-8089-b8756abebe52 | -11.6174 | -48.480598 | 2026-06-24 00:43:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e35c9bc3-3a59-31d6-bb09-30bfb567f976 | -6.3764 | -43.5896 | 2026-06-24 00:43:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12d41c2a-8304-3667-8a15-a98b16d3dce5 | -7.5969 | -46.4701 | 2026-06-24 00:43:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71f9d127-0a94-3071-9edd-ae5a0bed3df1 | -5.7363 | -49.0853 | 2026-06-24 00:43:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1560811-715b-3415-977f-e8f37c28d05e | -5.8168 | -45.044701 | 2026-06-24 00:43:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0df1f33-4db5-3248-9769-769d7396a37d | -12.7892 | -44.451 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0203728-8748-3a19-ae3a-cd66f4e0a0f7 | -6.5951 | -43.898998 | 2026-06-24 00:43:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01110763-0cd2-377b-a368-7aa2f6a65c61 | -13.0607 | -53.3437 | 2026-06-24 00:43:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7112d2de-060e-313a-b416-efcaa3c554d6 | -9.3703 | -50.540401 | 2026-06-24 00:43:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d76fdefd-6621-3938-b4e0-b29df669293f | -9.444 | -40.363098 | 2026-06-24 00:43:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 175725d7-9bf5-3511-8172-92d243bcac1d | -17.2628 | -46.322899 | 2026-06-24 00:43:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 53433165-9368-3b66-9d11-5e29224dc808 | -7.365 | -47.024101 | 2026-06-24 00:43:00 | METOP-C | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eba77d1a-bfe9-3710-bf5d-a257a5a23c8e | -9.458 | -40.3778 | 2026-06-24 00:43:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f1d19f6d-87f7-338d-84ac-619e9393f7a2 | -10.6969 | -49.613098 | 2026-06-24 00:43:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f00cbeb-737e-3f9f-b9d5-b055a2e0cd0c | -8.6916 | -47.853298 | 2026-06-24 00:43:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 185586da-2ebf-327a-bdf1-12085f65ebfc | -8.6114 | -45.999001 | 2026-06-24 00:43:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e6434bb-b8b8-34f4-b875-6595f7f410c5 | -6.2568 | -49.876801 | 2026-06-24 00:43:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa69baf-76a1-327e-b3c7-3adbb2356cfb | -12.8409 | -44.364799 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 40357c8d-dc3e-3574-80f9-36ce0681f1d0 | -9.4379 | -48.865601 | 2026-06-24 00:43:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83154e5b-4bf5-3deb-bb4f-6b1cbe715306 | -6.9925 | -42.899502 | 2026-06-24 00:43:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 16280316-6e5f-3b27-80fe-9a3c803b0100 | -6.3844 | -44.8293 | 2026-06-24 00:43:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a149ca1f-3d5a-35ee-862f-df48ee55d66b | -9.4624 | -40.395 | 2026-06-24 00:43:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 898cb5f1-1c92-3163-b97d-1fd011098c70 | -12.783 | -44.425098 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 00116dcd-2db7-3e42-9fb5-020e59e501af | -12.785 | -44.433701 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 235ffb29-2cfd-367d-ac59-6657e6d3001b | -9.2151 | -47.932499 | 2026-06-24 00:43:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c934d22-ef27-32a6-a531-6ab01d391021 | -12.843 | -44.3736 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 756d7957-bb8b-3725-a604-300666e29036 | -4.3486 | -47.760502 | 2026-06-24 00:43:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f911d45-5e26-3858-943f-2e6be819b210 | -12.8527 | -44.371201 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ae062cb0-56d0-3978-9b9c-0860ea2de3f9 | -10.6985 | -49.620201 | 2026-06-24 00:43:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8dfd0122-c94a-355d-86fd-b7b464a34274 | -13.0729 | -53.3531 | 2026-06-24 00:43:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c15d43dc-a526-31e3-a438-3cd59fd74ec0 | -4.2818 | -48.364498 | 2026-06-24 00:43:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a516d8f8-0285-3a2f-9536-2557e7029c09 | -11.4886 | -46.739601 | 2026-06-24 00:43:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e24e8d3-0db9-3a30-8dd2-fb5ef3d77747 | -4.3374 | -48.964802 | 2026-06-24 00:43:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd9a03c3-b55e-3159-b203-4602e4a14094 | -3.9585 | -43.1203 | 2026-06-24 00:43:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f1b14ad-e62a-3529-98e0-24edbee824b3 | -11.2602 | -43.342999 | 2026-06-24 00:43:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e6f2e7ec-54c5-3ae9-bbb3-9b2f891d3959 | -12.7732 | -44.427502 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a662a7ff-fef3-3a3b-8461-53de30047c54 | -7.9606 | -43.916302 | 2026-06-24 00:43:00 | METOP-C | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4d7837-8a77-3e13-8372-fc7f7771f5f4 | -11.2407 | -43.347801 | 2026-06-24 00:43:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6577a5c0-931c-34ac-9519-f7660b2b14c9 | -9.5856 | -49.108898 | 2026-06-24 00:43:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 510bdc83-a08a-39c6-8097-8239f065afaf | -8.6095 | -45.990898 | 2026-06-24 00:43:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bb3dee4c-f584-39db-bd11-6019e18e6462 | -4.3504 | -47.768002 | 2026-06-24 00:43:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54ab4845-1183-3398-955b-e2583e2a1872 | -12.8311 | -44.367199 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a5395e9-c856-3775-8ea0-100bcae69a5f | -12.7871 | -44.442402 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b65b17a-3083-37ea-b0ca-13095a50c311 | -11.2505 | -43.345402 | 2026-06-24 00:43:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 557019a4-3ad3-32d2-b8d3-eb40355a30cc | -8.6076 | -45.982899 | 2026-06-24 00:43:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 387dc4df-7a5f-3ead-ba4d-748dcb919d35 | -12.8506 | -44.3624 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a953e64e-c31e-3ecc-909f-b6215b89dc1a | -17.615 | -46.699299 | 2026-06-24 00:43:00 | METOP-C | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0c3cd773-fbc7-3b0b-8ffd-5e7f379c75ee | -9.3719 | -50.547798 | 2026-06-24 00:43:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef7a0215-15e5-30f8-8dee-be67ed4450b6 | -12.7752 | -44.4361 | 2026-06-24 00:43:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9f1dceb5-ef3f-3e63-abf3-4a398a2010b5 | -10.1072 | -47.550201 | 2026-06-24 00:43:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eb52b906-6ae9-3226-8a7f-7c8692d4db4b | -11.619 | -48.487598 | 2026-06-24 00:43:00 | METOP-C | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ba57552-61f7-331c-b523-fc40d5e26bee | -6.3541 | -43.5826 | 2026-06-24 00:43:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0c92505-eee7-3eb6-89ba-4cb0b8bc58ca | -5.8116 | -45.066299 | 2026-06-24 00:43:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| db6cc979-ce53-3e2b-bb36-41c27126651f | -12.5156 | -48.260899 | 2026-06-24 00:43:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d50b3620-4680-3714-a3c4-7110043807b9 | -6.3638 | -43.5802 | 2026-06-24 00:43:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6acbb4dc-0b47-32c0-a7d7-60191021884f | -9.2135 | -47.925499 | 2026-06-24 00:43:00 | METOP-C | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f934f2c5-bc69-3d4a-9e42-985e178ea9ab | -7.295 | -46.238602 | 2026-06-24 00:43:00 | METOP-C | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README4.md)
