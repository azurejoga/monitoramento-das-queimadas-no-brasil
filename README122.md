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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c077a8b-2127-302c-8e34-d63d5e28ba83 | -12.8259 | -47.9486 | 2025-09-13 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 582f990f-ccf6-35f3-a9af-926e0c62fd29 | -7.4322 | -44.4194 | 2025-09-13 11:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 44e253dd-57c9-38f4-9382-5d04998271cc | -11.7204 | -46.5579 | 2025-09-13 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| c15e99ba-cbfc-3754-96c4-ee0022e00c11 | -16.3422 | -51.5217 | 2025-09-13 11:50:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0c1220b6-e9aa-3444-bd75-2d6ba8c81e43 | -16.4906 | -55.1276 | 2025-09-13 11:50:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 43635d9b-0ee3-320c-b5f0-82dc612b9ac3 | -15.8213 | -52.2015 | 2025-09-13 11:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| a9013512-b82e-37d5-8ec5-f23f2cc2eb77 | -11.4836 | -43.6875 | 2025-09-13 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 95872c90-1ae7-39d1-b567-fe77f211cf28 | -12.8456 | -47.9236 | 2025-09-13 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 314.3 |
| e8d306c7-3fe9-394f-a380-5a8d21b6233f | -15.8648 | -47.2322 | 2025-09-13 11:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 75359b09-dfc1-3940-802b-71c296bc7a69 | -18.0071 | -46.9266 | 2025-09-13 11:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 178dd044-2d29-3b39-9e09-29c8838823a5 | -11.7826 | -47.402 | 2025-09-13 11:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 84.9 |
| d5487cf1-5058-338a-8be0-fff5dc4c1abe | -9.0544 | -45.8036 | 2025-09-13 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 200.5 |
| 1edcd133-c910-37bf-b372-241772ec658c | -14.4204 | -47.3011 | 2025-09-13 11:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 175.9 |
| e0939b04-5038-3478-b81e-38516a3ff577 | -14.4398 | -47.2979 | 2025-09-13 11:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 100.7 |
| ba0bf55f-2c65-361a-956e-6141255ae0b8 | -14.4199 | -47.3238 | 2025-09-13 11:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 06d6a1c7-6d03-3b6a-aa5f-dc20c3ff7828 | -11.4832 | -43.7112 | 2025-09-13 11:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| e42e94f4-87d1-3edb-a806-069244cf0436 | -11.7391 | -46.5779 | 2025-09-13 11:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 9286fc03-021d-3660-ac4b-22e2349cf463 | -9.2656 | -59.4191 | 2025-09-13 11:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c7a51e83-c85f-3bae-895c-8241eb373fc4 | -14.29 | -46.0924 | 2025-09-13 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 95.6 |
| b6e826f4-0f01-3ddd-ad6f-ee64e65a4f8b | -14.2905 | -46.0693 | 2025-09-13 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 7c9212bf-9b6f-36a0-be1a-972017ab9044 | -14.2092 | -46.2439 | 2025-09-13 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 70f8014e-cab4-3e90-8160-c573cd27fd2b | -9.0541 | -45.8262 | 2025-09-13 11:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 209.2 |
| 54b90bef-473c-34b9-8f4a-a2b25c3d74fd | -12.8263 | -47.9263 | 2025-09-13 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 693b3eed-9a39-35f3-822f-ef535161ca5b | -12.8452 | -47.9459 | 2025-09-13 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| b85f3043-ac92-308e-8351-87027f525fc6 | -14.31 | -46.066 | 2025-09-13 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 26b57f42-c9ba-34d3-adb8-afcda46bfb86 | -14.1694 | -46.2965 | 2025-09-13 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 307.5 |
| b7225aae-f123-3830-9dec-a58d453af3b4 | -14.4199 | -47.3238 | 2025-09-13 12:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| a1328869-6c28-3cbf-a7d0-f13ad436108a | -14.31 | -46.066 | 2025-09-13 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 158.3 |
| e8d7a974-f4d7-3daa-8e8b-84f60517bbd4 | -14.2905 | -46.0693 | 2025-09-13 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 140.1 |
| eec928cd-87f9-3640-a4cc-16d238f7e228 | -11.8094 | -50.5428 | 2025-09-13 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| a076b86e-661a-374d-9bf5-0c4de6193a02 | -12.9402 | -47.9991 | 2025-09-13 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 5ee78382-d2bb-38d9-874d-018cab8e36c6 | -11.3926 | -50.4619 | 2025-09-13 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 63bd11cd-02ee-3b97-bcc1-c52520aaee0b | -12.9398 | -48.0213 | 2025-09-13 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0abbd60b-49dd-36e1-91ef-b27cae648ae7 | -12.8456 | -47.9236 | 2025-09-13 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 36fb10d6-b349-349e-b412-fb3c291b8721 | -11.7903 | -50.545 | 2025-09-13 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 600eb4c0-938c-31a2-bf48-f4f167f089af | -9.2658 | -59.3997 | 2025-09-13 12:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 88a3705d-2ed0-35b3-b251-4faaadfb75f2 | -11.4119 | -50.4383 | 2025-09-13 12:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 39ff565d-3ba4-3193-bd80-86f16b08635a | -14.4398 | -47.2979 | 2025-09-13 12:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 42995f39-ae3e-3d53-9eba-cc7209777f16 | -14.2092 | -46.2439 | 2025-09-13 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 279.9 |
| f1496d38-f05c-37f1-841c-8d5ffe189999 | -9.0544 | -45.8036 | 2025-09-13 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 81d125d7-fe6c-30fc-afff-cbd63546b171 | -14.2277 | -46.2866 | 2025-09-13 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 92afd5c2-0691-30ea-a342-4c5968fc7549 | -12.8452 | -47.9459 | 2025-09-13 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 8dd285a0-1bb9-3028-b6f2-109f4c1e8a10 | -11.7826 | -47.402 | 2025-09-13 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 7ca4e290-112c-3f7c-ab31-94ca12956d45 | -14.4204 | -47.3011 | 2025-09-13 12:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 178.0 |
| 20e8c653-202a-3200-9467-5a90f0628144 | -14.4394 | -47.3206 | 2025-09-13 12:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| f2e117a9-4ce9-3938-9c57-ad2d27252d02 | -15.4517 | -47.3291 | 2025-09-13 12:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 9370a572-a02f-3d87-b101-a86517bcd842 | -12.8263 | -47.9263 | 2025-09-13 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 215.2 |
| dfc325fd-7fba-3d3c-be54-95938f199df1 | -14.1698 | -46.2735 | 2025-09-13 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 292.0 |
| 22a13262-bbd7-309e-a380-43bf5a657776 | -10.9283 | -47.2223 | 2025-09-13 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 4f28a849-56fb-38d3-a91e-a5c194bc2d6c | -11.8284 | -50.5406 | 2025-09-13 12:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 718e15ec-8aed-35a1-908a-839f9c3bb8f6 | -15.8648 | -47.2322 | 2025-09-13 12:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 3cdc11d8-c37b-3458-84cb-7953c2131739 | -14.1893 | -46.2702 | 2025-09-13 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 283.1 |
| 0f7660c7-152d-322c-8e92-ce6d6f9b4b7e | -17.1549 | -48.4908 | 2025-09-13 12:00:00 | GOES-19 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 457.3 |
| 95e148a1-d0be-3fcf-8df5-d130fb149bd7 | -16.3422 | -51.5217 | 2025-09-13 12:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f6cce78d-2235-3a56-8d88-306d386966ea | -14.2083 | -46.2899 | 2025-09-13 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 171.8 |
| 70c62ac3-2a8b-3241-99f1-b8fddc9a16b6 | -12.8259 | -47.9486 | 2025-09-13 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 276.1 |
| 13981ce5-29cc-3464-8df8-0db037f06aaf | -14.1694 | -46.2965 | 2025-09-13 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 394.6 |
| e181d172-d89a-37f4-95be-6d9611bca0f4 | -15.4713 | -47.3256 | 2025-09-13 12:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 07b47cad-c1c0-30f6-9bf1-8325bc44279d | -14.29 | -46.0924 | 2025-09-13 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 0f54de8f-6444-3353-bbfe-ffa7e4019124 | -9.0541 | -45.8262 | 2025-09-13 12:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.9 |
| cd221eb2-0aca-3245-900d-1db83a9fe587 | -7.4322 | -44.4194 | 2025-09-13 12:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 134.3 |
| eedb56d7-11ae-332a-8b51-2fe940922bec | -14.2097 | -46.2209 | 2025-09-13 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 40474ea1-1dae-3582-8ef9-7f83261e9996 | -9.2656 | -59.4191 | 2025-09-13 12:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 92cc71f5-e189-31a9-bab0-8ad0cc653b45 | -14.2088 | -46.2669 | 2025-09-13 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 10aae834-6820-3d2e-a443-28c6b427167a | -15.8213 | -52.2015 | 2025-09-13 12:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a83dd665-11f4-3edc-9494-c2074b61dc8c | -15.8213 | -52.2015 | 2025-09-13 12:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 78.0 |
| e343764b-e39f-37ae-a33c-c15a0323d8c4 | -13.8979 | -48.2804 | 2025-09-13 12:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 9262ab63-e47d-3774-a158-2b0a57e76817 | -11.7826 | -47.402 | 2025-09-13 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 2b9e8834-198e-3bbf-8985-a82f1f6d4367 | -13.9172 | -48.2775 | 2025-09-13 12:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 0259580c-d933-3470-b365-fade158aa859 | -12.8259 | -47.9486 | 2025-09-13 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 211.6 |
| 4bb6dabb-59b9-35a0-b7d8-534948b4f535 | -15.1601 | -50.1379 | 2025-09-13 12:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 620f0fde-f940-3ce6-942a-935b29b9c00d | -15.4517 | -47.3291 | 2025-09-13 12:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 957fa54d-57e4-3e33-a271-8ea853a695a5 | -8.9595 | -44.4436 | 2025-09-13 12:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 22e60e20-fd10-3a69-aaa4-8c2a147dab94 | -14.29 | -46.0924 | 2025-09-13 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 116.4 |
| dd47205e-b15e-3238-a345-41760433393b | -18.0065 | -46.9499 | 2025-09-13 12:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 2e04ea28-4fa0-3169-b9be-e437c292431d | -16.3422 | -51.5217 | 2025-09-13 12:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 69c812c1-7709-3268-adc6-a5c5c46df82d | -15.4713 | -47.3256 | 2025-09-13 12:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 48e34b44-c638-372d-a982-9cddd53c3bed | -14.2905 | -46.0693 | 2025-09-13 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 91dfebe0-2811-3fea-bab1-8bfe5cee1737 | -7.4322 | -44.4194 | 2025-09-13 12:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 97d94c02-80bd-36a7-9d34-f0b9f94f9a23 | -12.9025 | -47.96 | 2025-09-13 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| bff04d98-d44a-3410-b7b1-2aa63c7ebd8f | -14.4398 | -47.2979 | 2025-09-13 12:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 325.9 |
| b7689023-ca6a-3aeb-97ad-d962b60faa3d | -11.7391 | -46.5779 | 2025-09-13 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 8b5a85ec-7757-3ecc-9cd8-41a95667ff3c | -9.2656 | -59.4191 | 2025-09-13 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| e3b35207-905a-32aa-9445-589ceb3d328d | -13.2222 | -51.7382 | 2025-09-13 12:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 3efcb1a4-93ab-357a-8baf-3ef5dba54474 | -12.8452 | -47.9459 | 2025-09-13 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 175.5 |
| 9289f2e3-2a36-302c-a375-97e213c783c9 | -14.4394 | -47.3206 | 2025-09-13 12:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 163.8 |
| be217864-aaf2-3289-b17d-5a9c6241b3f3 | -15.8648 | -47.2322 | 2025-09-13 12:10:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 28f36aea-89f6-30fe-bcfa-6a5a88484465 | -11.7204 | -46.5579 | 2025-09-13 12:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 282b55e2-9d38-3e64-bdc7-c8fdd4b64f89 | -12.8263 | -47.9263 | 2025-09-13 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 174.4 |
| ce99ad10-9271-355b-b700-576c1d8f5c83 | -14.4204 | -47.3011 | 2025-09-13 12:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 429.4 |
| 1ce62aef-c841-3f63-ada8-982fa7f8154e | -9.2658 | -59.3997 | 2025-09-13 12:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 4d1aef79-c53c-3220-8a6e-208c31b60a38 | -12.9398 | -48.0213 | 2025-09-13 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c8d788f3-1361-3c3d-9611-6a60e0aba0e5 | -12.9402 | -47.9991 | 2025-09-13 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 97a02835-a122-30b3-92ef-2919e03e5a9f | -15.1597 | -50.1598 | 2025-09-13 12:10:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| e82eaf63-4f7d-33aa-91db-01054e9e7b8c | -14.4199 | -47.3238 | 2025-09-13 12:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 197.7 |
| da4822f5-4584-32e4-ae58-8d6a73943f8a | -12.1236 | -47.579 | 2025-09-13 12:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 5dc6876d-4b48-38c7-90af-2df2ed32d7a6 | -13.9185 | -48.2105 | 2025-09-13 12:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 1f5430f2-8073-31e0-b5c8-711f5bd98573 | -14.31 | -46.066 | 2025-09-13 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 059196a8-5626-3095-8dd6-d312dcec039d | -12.8456 | -47.9236 | 2025-09-13 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 256.5 |
| d0d7a9f4-2e00-3cb4-abec-0279d304f2ee | -17.1549 | -48.4908 | 2025-09-13 12:10:00 | GOES-19 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |


[Clique aqui para ver as próximas entradas](README123.md)
