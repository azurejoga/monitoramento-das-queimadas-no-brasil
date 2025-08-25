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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0ceb0a8-fa7f-358f-9bdc-9a0878a0338b | -19.20283 | -51.0936 | 2025-08-25 12:19:00 | TERRA_M-T | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b8830572-c88f-35ed-a6d0-3015fa8bdc58 | -19.9193 | -44.62907 | 2025-08-25 12:19:00 | TERRA_M-T | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| 42721582-dbb1-3d7a-8f83-d656d959e186 | -20.35442 | -46.7137 | 2025-08-25 12:19:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| bd39d4ae-030e-3953-8a4b-8cb2e4852886 | -20.35302 | -46.72414 | 2025-08-25 12:19:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 24fe72db-f55d-3811-a520-76799919b39f | -20.77802 | -44.30181 | 2025-08-25 12:19:00 | TERRA_M-T | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 41ed1617-7180-3a5d-83be-d7db7e6603ab | -19.19317 | -51.09197 | 2025-08-25 12:19:00 | TERRA_M-T | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 176fc6a4-7bcb-385e-90f0-8e839d0f3c06 | -21.74883 | -45.05379 | 2025-08-25 12:19:00 | TERRA_M-T | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 7b592232-00ab-3c01-a817-c108cefc12d6 | -21.14833 | -42.17284 | 2025-08-25 12:19:00 | TERRA_M-T | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| be371580-fd4e-38e9-b7b4-6fee9b728120 | -19.91776 | -44.62177 | 2025-08-25 12:19:00 | TERRA_M-T | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| a903fd0f-f588-3f32-85e2-25d196f2a8d2 | -20.3016 | -47.17281 | 2025-08-25 12:19:00 | TERRA_M-T | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9b572b87-bf39-3e69-a238-9f9becbabf45 | -20.30028 | -47.18254 | 2025-08-25 12:19:00 | TERRA_M-T | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7d503f8b-6f52-3486-9b8b-e8a59d4b9d4c | -20.68678 | -46.83794 | 2025-08-25 12:19:00 | TERRA_M-T | PRATÁPOLIS | MINAS GERAIS | Brasil | 3152907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0fc912ef-3d63-3959-a1b9-1a156fa95078 | -21.19134 | -45.28631 | 2025-08-25 12:19:00 | TERRA_M-T | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 1cf967f8-07b5-3cb5-a356-807a93ab1eab | -21.75038 | -45.04098 | 2025-08-25 12:19:00 | TERRA_M-T | SÃO THOMÉ DAS LETRAS | MINAS GERAIS | Brasil | 3165206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| bbcb581a-5461-3b60-ac34-5e5bac23afec | -20.16891 | -41.3546 | 2025-08-25 12:19:00 | TERRA_M-T | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| dcff151e-2502-31bd-9816-8d15fe6d4634 | -21.82833 | -45.40401 | 2025-08-25 12:19:00 | TERRA_M-T | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 454673b5-fbfc-3232-bf4e-4e81e2849d02 | -14.5072 | -51.9354 | 2025-08-25 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| e3793c1a-cb1b-30ed-8305-6f60f8d9fb61 | -11.6093 | -46.3472 | 2025-08-25 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7fba0af6-8733-3ca7-b07c-940799055d5d | -14.5076 | -51.914 | 2025-08-25 12:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 236.7 |
| 9999eaf3-1299-36cc-b8d1-86a44361a0d3 | -8.9874 | -65.4192 | 2025-08-25 12:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 976dca74-4133-35e7-8e4c-1daf671b6871 | -11.6089 | -46.3699 | 2025-08-25 12:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| aecfb547-5502-30f6-883b-320029341bdb | -12.6937 | -47.8339 | 2025-08-25 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 7b310de1-511c-31a5-9e44-698d0ec39e7d | -8.5758 | -62.6323 | 2025-08-25 12:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 125.6 |
| d6261ad0-8557-3728-9a56-aca2381a1fc1 | -12.3078 | -49.1421 | 2025-08-25 12:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 19fd28ea-bc2b-3248-b398-a5a5072899ea | -8.8734 | -62.4495 | 2025-08-25 12:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 81.0 |
| bcb27569-6c6c-30d4-843e-1ae0269be5a3 | -11.6093 | -46.3472 | 2025-08-25 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 9b51d589-e02c-3184-87f8-929bba3dfbb8 | -14.5076 | -51.914 | 2025-08-25 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 176.7 |
| 6052c900-076e-3d97-a42f-20db9e5b89cc | -8.8735 | -62.4305 | 2025-08-25 12:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 38a4be9b-0927-3027-a71b-bb805797b821 | -11.5898 | -46.3725 | 2025-08-25 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 847421a2-610a-3c7d-a087-ee3283d41cd0 | -8.9689 | -65.4198 | 2025-08-25 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| a2f3ca21-b546-3de8-b1c2-3b549bcc896a | -8.5759 | -62.6133 | 2025-08-25 12:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 2811000e-3236-38d7-8955-8ef2ee4bc9e4 | -11.6089 | -46.3699 | 2025-08-25 12:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 179.3 |
| 6e73a63d-a5a0-3a3a-8447-35ed0e605216 | -14.5072 | -51.9354 | 2025-08-25 12:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 102fafa3-f49c-38e9-be24-9e551942d853 | -8.9874 | -65.4192 | 2025-08-25 12:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 1d220000-65b2-388c-9148-95b8be8c9767 | -12.6937 | -47.8339 | 2025-08-25 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.6 |
| a22e93a6-33b9-3add-97a6-6d77f13f40ab | -8.5759 | -62.6133 | 2025-08-25 12:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 111.2 |
| b55dd4fb-930f-3886-bbeb-ed6e77ad4145 | -8.5758 | -62.6323 | 2025-08-25 12:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 185.8 |
| 5ab856e9-361b-3550-81fa-e599a2d0ba8c | -11.6089 | -46.3699 | 2025-08-25 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 58d62a01-4e10-324a-b448-c0d71e400a35 | -14.5076 | -51.914 | 2025-08-25 12:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 1b457bd7-2c99-3b0c-a271-9617cbc7d1d6 | -11.6093 | -46.3472 | 2025-08-25 12:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 049440e3-6e8c-3b15-b7aa-8f9bc3642723 | -8.9874 | -65.4192 | 2025-08-25 12:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 143.0 |
| 5dbce386-fdfb-3a2f-80fe-61a382721567 | -12.6937 | -47.8339 | 2025-08-25 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 5c85ab23-474f-3618-bb08-4f6ba0efbfef | -8.8734 | -62.4495 | 2025-08-25 12:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 2578199f-43a3-3e90-8a18-1ae59adaf264 | -8.8735 | -62.4305 | 2025-08-25 12:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 31958444-011c-3bab-b350-e946f781463a | -8.9689 | -65.4198 | 2025-08-25 12:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| fcd37b2b-97e6-3acb-a541-497fd0d833a7 | -9.1722 | -59.4629 | 2025-08-25 12:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 278d1147-c851-339c-b251-6fddfadae6ac | -5.6443 | -45.1373 | 2025-08-25 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 36e2e51f-eb2e-3cb9-9d27-e97443e79eb6 | -8.9874 | -65.4192 | 2025-08-25 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 222.5 |
| 74f8e5d9-c9d6-3efb-b930-70b77a406c18 | -3.4542 | -43.3386 | 2025-08-25 12:50:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e48d3fd4-8dac-34bf-b9f1-84f41be892d9 | -11.6089 | -46.3699 | 2025-08-25 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| dbb4aff6-24b6-3424-ae50-0062ffa6eb02 | -8.9689 | -65.4198 | 2025-08-25 12:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 3f052940-c3fc-3cfc-a8d9-e25460037dac | -8.5759 | -62.6133 | 2025-08-25 12:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.2 |
| ee3c897e-f202-3037-ae34-d2d0fb972938 | -9.2092 | -59.4997 | 2025-08-25 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| d8a01222-2fcd-3cb2-a0f5-ad2b904fc2ca | -11.5898 | -46.3725 | 2025-08-25 12:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| cd2956bc-e5a8-33b0-8c3d-e14806745581 | -11.6304 | -46.2311 | 2025-08-25 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| b35c52bc-8994-36f8-b564-649476ae2030 | -11.6093 | -46.3472 | 2025-08-25 12:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| da3bb050-e7db-3148-bba2-5e744cb04875 | -11.5441 | -50.4876 | 2025-08-25 12:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 3d201dce-3a15-37ec-9858-73f8180c7ca1 | -7.904 | -45.8986 | 2025-08-25 12:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 9ab7d248-7d31-3b59-bf50-d49213ab53f5 | -8.8734 | -62.4495 | 2025-08-25 12:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 101.6 |
| e68cb21e-7113-3a77-b4d4-3339d49c0407 | -8.8735 | -62.4305 | 2025-08-25 12:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 95.0 |
| d4705a46-33db-3af1-9a0d-5c9f245c5a86 | -9.1906 | -59.5007 | 2025-08-25 12:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| b046cca7-4d76-38d3-a716-4de7f57e7c3a | -8.5758 | -62.6323 | 2025-08-25 12:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 148.4 |
| 1f720f71-9809-38ed-ba4d-2243059b880b | -5.6817 | -45.1347 | 2025-08-25 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 83b89830-8713-37af-b654-2bccc14b0571 | -11.6089 | -46.3699 | 2025-08-25 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 3e91de85-29c2-3518-a5e1-9a5e590b2cff | -10.5364 | -46.7568 | 2025-08-25 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| a9a02b06-d856-3972-ad67-0c53ba8e9b8e | -8.5758 | -62.6323 | 2025-08-25 13:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 12c750db-eb9f-317c-8472-5195b0241065 | -9.1722 | -59.4629 | 2025-08-25 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| eb530b6f-3b2c-34fc-8d4f-19c3672ea963 | -8.9689 | -65.4198 | 2025-08-25 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 5afc305a-9e96-3ec5-8615-bb2e22ee203b | -10.5874 | -47.1527 | 2025-08-25 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 38f76ad6-e13c-3a64-b5a1-d11099ec86a6 | -8.8735 | -62.4305 | 2025-08-25 13:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 6522afc8-cee8-32e4-b62b-1e1fc06ca38f | -12.3078 | -49.1421 | 2025-08-25 13:00:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 07e1606b-8f74-33e8-a7db-ec9a9f354c1e | -15.1448 | -59.6037 | 2025-08-25 13:00:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| da231dad-049b-395a-9968-14e5f8ed9d40 | -8.5759 | -62.6133 | 2025-08-25 13:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a20ad52d-5b98-3e5e-90aa-d591f71e4d1b | -9.2092 | -59.4997 | 2025-08-25 13:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 958e737f-3cb9-3f59-b99a-54daec152366 | -3.4542 | -43.3386 | 2025-08-25 13:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 0b5ea807-a372-3226-be4d-c98bc92b741b | -8.8919 | -62.4487 | 2025-08-25 13:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.1 |
| c5b32e63-57e7-3759-ba28-d7fc6814cccf | -3.4541 | -43.3618 | 2025-08-25 13:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| d5d8b783-af59-3cf6-a3d2-d846a90ec3e8 | -11.6093 | -46.3472 | 2025-08-25 13:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d873f7f9-b7a5-381b-8f80-4e6e3f776748 | -8.8734 | -62.4495 | 2025-08-25 13:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| caefbbd4-fc63-3fb5-83a9-af3d98fa43c1 | -9.006 | -65.4 | 2025-08-25 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 396fce2e-42bc-39eb-a69c-ea1b166e4aef | -8.9874 | -65.4192 | 2025-08-25 13:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 259.1 |
| 1868c85f-8465-32ec-8a1d-a655e4afb13c | -10.7015 | -47.1388 | 2025-08-25 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| a9a42b23-5581-3c27-90eb-e1b57e3de30d | -9.324 | -48.2633 | 2025-08-25 13:00:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b5475364-ad1a-349b-8b9a-2f2fc08d13cd | -14.9051 | -45.5439 | 2025-08-25 13:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 2dae91bf-419d-3541-8c78-0eb530230bc0 | -8.5758 | -62.6323 | 2025-08-25 13:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 115.8 |
| d1ad354b-38fe-3142-9959-826c55099924 | -11.6089 | -46.3699 | 2025-08-25 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| f145ef51-22af-34db-b6a6-535d659b9b4d | -9.1906 | -59.5007 | 2025-08-25 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 4198d880-3cc6-3615-a348-1d6d647b520f | -8.855 | -62.4313 | 2025-08-25 13:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 601335cd-f43c-3e32-9cf6-af995d052952 | -12.6937 | -47.8339 | 2025-08-25 13:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| ab0355f6-cdf9-38ac-919e-64b2da7316cb | -8.8735 | -62.4305 | 2025-08-25 13:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 142.7 |
| ceb97412-96a1-380c-ad96-c1789c4b5234 | -5.6443 | -45.1373 | 2025-08-25 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| a300331f-2ce1-3f11-8d65-43f56a269898 | -3.4542 | -43.3386 | 2025-08-25 13:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 544ccbc9-bf49-347d-b70d-bf22c5834632 | -5.6815 | -45.1573 | 2025-08-25 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 204ebb33-bf60-38d3-9625-3cb1954c1eee | -9.006 | -65.4 | 2025-08-25 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 8f8a1299-0f45-3855-8285-7b3243ee0d90 | -11.6093 | -46.3472 | 2025-08-25 13:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 36c7d7d8-9f08-3a9a-abac-c38ea7f47f73 | -10.5878 | -47.1304 | 2025-08-25 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 754fa7c1-95f8-3b39-81da-06c32e8129d4 | -3.4541 | -43.3618 | 2025-08-25 13:10:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 3c75afdf-9ab6-3fa0-90e1-8979c8113d96 | -8.8734 | -62.4495 | 2025-08-25 13:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 125.2 |
| d84595f8-ff32-35b9-9d85-c39242c3816c | -8.9874 | -65.4192 | 2025-08-25 13:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 268.0 |
| f5539aac-509b-347b-aa90-bf5f1d6b4745 | -9.209 | -59.5191 | 2025-08-25 13:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |


[Clique aqui para ver as próximas entradas](README96.md)
