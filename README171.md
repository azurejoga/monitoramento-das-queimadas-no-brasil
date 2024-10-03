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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 060daf25-c467-3719-b656-36e12a0061fd | -9.55533 | -64.26167 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e5311cc-bc28-3d1f-9b31-76b52da17dc6 | -9.55228 | -64.25597 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53acb92c-ea9a-3802-a16d-73e6c58d1581 | -9.55206 | -64.25863 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 058f5b1c-c0a5-3e1c-b6dd-524ab27a5208 | -9.54898 | -64.25291 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 179904f3-9669-339e-9516-acdcd551b1c9 | -10.7064 | -64.14912 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8683fc11-67c1-378b-a0bb-bf16668e7394 | -10.70559 | -64.15382 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b2c2b2d-1777-377e-a639-54d2b9cde819 | -10.70255 | -64.14854 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e54e11c4-a392-3f96-bacc-0777f6f6341f | -10.70173 | -64.15332 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3c5637c-ade0-312f-a705-a893b057d324 | -10.69786 | -64.15286 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fa592daa-8795-302d-b7fe-a6ee3d11fed4 | -10.69702 | -64.15778 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 7271e748-8e09-302b-9f09-6fc9f0172f30 | -10.694 | -64.1524 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae208395-50d8-3b2c-ae5a-54c83efdaeb1 | -10.69316 | -64.15723 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f257fde4-b959-3e8c-a657-9111bf290b51 | -10.69015 | -64.15186 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c310cf-9dbc-30f6-ad7b-58abaa07f718 | -10.68931 | -64.1567 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5986d719-d81c-3305-93b9-7b0e7d33b6a6 | -10.61917 | -64.51484 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 737e19c2-0362-31ec-a076-918c211a2837 | -10.60078 | -64.41029 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08af6042-056a-3061-b82f-8dfc4e00d3bb | -10.59603 | -64.41465 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b03c73fe-2c40-3eb4-9429-8df525380418 | -10.10789 | -64.42015 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b2a26722-a9dc-3b00-8e36-bcadcc2a5e60 | -10.05776 | -64.4095 | 2024-10-03 05:16:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2afb0f31-0a36-3aca-baea-a588c4411998 | -10.69849 | -63.49039 | 2024-10-03 05:16:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26e98a3f-1aee-3972-a341-68aa15416627 | -10.2644 | -63.33447 | 2024-10-03 05:16:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 750691c7-bf42-38c9-a261-a2f2750736d1 | -10.26367 | -63.33886 | 2024-10-03 05:16:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9303b7cb-3485-39ad-94f1-a990da8820ee | -10.26362 | -63.33239 | 2024-10-03 05:16:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd3b1ec0-fdbf-3639-9fcf-5a65890a5763 | -10.26287 | -63.33677 | 2024-10-03 05:16:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0774478-fd72-383d-ada4-668885a67ecb | -10.26212 | -63.34116 | 2024-10-03 05:16:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68b24910-468a-31fd-a6a0-7554f9f572ff | -10.26144 | -63.32947 | 2024-10-03 05:16:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02dd52c9-3476-3f4f-9356-db530e0d4fc8 | -10.26071 | -63.33384 | 2024-10-03 05:16:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 699faaa6-dd2d-3516-94fe-67c2edaf1b9d | -10.25994 | -63.33178 | 2024-10-03 05:16:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b7c1c01-1bf0-3626-b735-ab75b0105aed | -11.97325 | -64.76646 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96da3a5d-4d9d-3596-a0dc-bf4bfb6664e0 | -11.96935 | -64.76574 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17099960-af47-36a2-b4e2-39a3ae225fbc | -11.76287 | -64.28561 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 94bb7991-a219-3462-bfbd-eb57a287a54f | -11.75908 | -64.2849 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9910eb21-b0d0-3bd2-b8f2-ce2e7f15944a | -11.75611 | -64.2794 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ec01c5c-bfae-3a9f-88a1-df46184f0cd4 | -11.75446 | -64.28894 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3959963a-dbb8-33aa-9052-1e3e5273c032 | -11.74894 | -64.18595 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9982058d-14b2-31d3-a194-e0a516c44c85 | -11.74516 | -64.1853 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 764afcc0-43fd-3f18-908a-91127ceff740 | -11.74137 | -64.18465 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44432cec-494f-31aa-b815-da683ddbe471 | -11.73325 | -64.11887 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d75d46dc-acc7-3a85-a42b-a5353810a278 | -11.73088 | -64.13283 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08be3d89-36bf-3ee0-93fa-4f38f5c72237 | -11.73009 | -64.13748 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 341559ef-f084-30b8-9797-7501b8dc6f42 | -11.72632 | -64.1368 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d49a7b74-ded5-357b-bdb7-27849f189471 | -11.72404 | -64.28354 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5848feef-d529-3fc5-a729-489bdde64b7d | -11.72256 | -64.13611 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3996285-5d14-370e-83e6-e33fdade8bbc | -11.72138 | -64.28118 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9795e6f-e380-39ff-8019-b4f963fb0658 | -11.72058 | -64.28594 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c777dd6-3f33-3ed9-a531-42572576f86d | -11.71879 | -64.13544 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61ec7ba5-2a3e-38de-946e-a7e8e5e8619f | -11.71838 | -64.27578 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b67a90e1-ea8a-320c-8790-f803dd6836f2 | -11.71758 | -64.28053 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 955bad6c-24b7-3dd8-8ae4-fbabb51564af | -11.61984 | -64.1011 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2e166b9-4f5c-3b0c-9340-2458a47357f3 | -11.61687 | -64.09575 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d918626-a312-33e2-ae2b-cd5f3585ba71 | -11.61528 | -64.10506 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8829fbf1-b1ba-3ac6-89d0-392766c79597 | -11.61449 | -64.10974 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cf6bdf0-d59d-3539-a8ca-012574f890e5 | -11.61389 | -64.0904 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aff1ac3-9a19-3eff-b893-ec08b7578b7a | -11.60932 | -64.18601 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d790a74c-1be9-3161-8b6f-d46aa0e9b6d5 | -11.60852 | -64.1907 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c6f0aac-03ea-389a-bb0d-fbb05ba262ef | -11.60254 | -64.17999 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78688a0d-4328-31f9-b287-3b1a3eb8b730 | -11.59795 | -64.18401 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a5abb245-1545-3d13-8f83-2cd78d2606b2 | -11.59336 | -64.18804 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f7ae0649-453b-3dd6-bf89-a1a7ca50289a | -11.58288 | -63.76632 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5236e5f4-6465-3661-8a8e-b286e74a6b63 | -11.57996 | -63.761 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0a463260-ddda-3191-9e82-49124b1a8df5 | -11.57914 | -63.76586 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd7fff92-0b29-3f61-aa98-9386ba1c4bab | -11.57622 | -63.76059 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba238b0a-9907-393b-a795-5c19258cfec4 | -11.57248 | -63.76019 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15894a7e-2628-31b0-a0c7-144b89ba458d | -11.56876 | -63.75969 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8938c28-8e88-3bc1-92ae-163a9ed04d16 | -11.56351 | -63.7682 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30a3af79-3a4f-3736-96a7-9db2bfc2fd2d | -11.55981 | -63.76756 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 585d669f-5b43-38ff-873a-cdc1b92bc9ab | -11.55904 | -63.77206 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7fa12f4-3f17-3bfc-8e17-dad0d0adedb8 | -11.55775 | -63.73467 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9ebde509-d434-33d7-a9a8-43f3a434d867 | -11.55534 | -63.7714 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fef177cd-660f-3e35-a060-4d0b2b48ebec | -11.55458 | -63.7759 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4e7af37-6687-303f-a270-93dca88c535d | -11.55327 | -63.73867 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e1e8151-e3f3-348f-94fc-5c8af78d12a6 | -11.5523 | -63.78938 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 760d3816-0a29-39c3-8937-d19c0d554a6d | -11.54957 | -63.73803 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10b437f6-3c8d-3d94-a147-b9310ab1ddf4 | -11.54935 | -63.78423 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71b61da7-a8c2-3258-89fa-c1c21a0d7116 | -11.54483 | -63.94694 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 854723f4-8def-3d1d-8bfb-37f78abec3e0 | -11.54406 | -63.95153 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edbf4483-f1e7-39fd-b101-f27b13b78842 | -11.52014 | -63.70982 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a012c97d-fd9f-33c8-a510-6d03d63f956c | -11.50807 | -63.58688 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 998a39e6-d71a-314c-ada9-2ee3e2437c3c | -11.50513 | -63.58187 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6d924e3-b6f5-3e2e-9176-e41f0369b684 | -11.46016 | -63.33734 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f290b4c4-3d1f-32f0-b989-d3d46354aa89 | -11.45988 | -63.33485 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 902be623-06b9-3aee-86d3-878895143e51 | -11.45917 | -63.33917 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4afa4dfd-836e-3182-9a2b-b234c8ded35f | -11.45653 | -63.33673 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4679948-d356-3b06-80ff-6d499edf79a3 | -11.45625 | -63.33425 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e6027c0-2122-3e11-8462-99fb597c6d0c | -11.45579 | -63.34106 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b0beb37-8022-3702-a664-a78974ae2b45 | -11.45554 | -63.33856 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35af0810-be98-30a9-8e0b-0d7bb116a294 | -11.45482 | -63.3429 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5de0603-ab7b-3b8b-8d5d-abcf01a3497c | -11.4529 | -63.33615 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c0d8464-8ff2-3697-8bc1-953a04404c62 | -11.45262 | -63.33366 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09453362-bd64-3fbd-afe6-eebf02608dd8 | -11.45216 | -63.34045 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e9f5b10-7061-3b58-8b8e-04af742dce43 | -11.45191 | -63.33796 | 2024-10-03 05:16:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 40a8c743-bec0-3a8e-8e00-a286be3c7850 | -10.84997 | -64.17547 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e10926ff-aab3-35f8-8124-f4278a12618b | -10.84919 | -64.18005 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dd50bdc3-d7e9-3680-bb1b-a3166e6a63eb | -10.84447 | -64.18463 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 908a4eb9-d689-30fc-9712-b69794d9650a | -10.83665 | -64.20744 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb7550e0-fbf4-3f8c-bcb7-f23717e6f6b2 | -10.83599 | -64.18812 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d7182352-6cd1-336d-9dc8-cba741d27aa6 | -10.83584 | -64.21223 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68b18e18-f125-38d3-8510-0dc23d259938 | -10.8352 | -64.19279 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| cc1e404e-11ce-3de4-982f-ac28ab68bf40 | -10.8328 | -64.20689 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0ca1a954-318f-31a1-9939-cfd62c1b5652 | -10.83136 | -64.19218 | 2024-10-03 05:16:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |


[Clique aqui para ver as próximas entradas](README172.md)
