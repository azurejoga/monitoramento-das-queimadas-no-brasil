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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8dfa8d5e-000a-3768-877d-04087697d99f | -7.7417 | -61.22601 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf3f9a9a-fa21-31e9-b641-ae9ed80bd732 | -7.65153 | -61.1967 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ec38111-763a-3e9b-89f8-5958c98a4071 | -7.65097 | -61.2002 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fca6edc-ce31-314b-a276-d06e00a09601 | -7.6482 | -61.19617 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 88b4025f-cca9-38fb-952e-253aa833d49d | -7.64764 | -61.19967 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25d1cae9-59ed-3e57-81ec-68820fd64c62 | -7.64042 | -61.2021 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e63ecc93-ca97-32f0-82df-23ce2f7191d5 | -7.59276 | -61.23056 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0b4a8466-544d-30f1-9e34-58fc338e5e1d | -7.5922 | -61.23406 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 597dbf39-9d94-3c74-b1ce-369cdf212381 | -7.58942 | -61.23003 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 391aef5c-df1d-3031-8a22-482a9c502854 | -7.58887 | -61.23353 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 768cf272-3edc-3e85-a874-63d672546418 | -7.58609 | -61.2295 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52aefa7d-3264-3fa8-a09d-c0803ea9a20a | -7.58554 | -61.23299 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab3e8603-032c-3f2e-8004-b7b994b6ac01 | -7.82328 | -61.69359 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aff11472-f513-39aa-8ac4-4eba9b9e31e7 | -7.80717 | -61.64378 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b01ab76-2a0a-341d-800e-c7f651389a28 | -9.1532 | -61.24317 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efd75d23-131b-3332-925c-71c2d2e36a2a | -9.14708 | -61.19561 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a9a55c1-058b-3f83-8118-11815493d7e6 | -9.1305 | -61.30048 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 623eddb2-f26d-3872-a2ac-dba5b472a84b | -9.12717 | -61.29995 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50de9db9-4c27-3477-a6f6-5dacd708cdf5 | -9.12662 | -61.30345 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9735becd-8902-3f5d-8366-f0bfd4d04ddc | -9.11774 | -61.27335 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b7ee6d9-c217-34f2-859e-d70461a6b0d9 | -9.11719 | -61.27684 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8cfadd0-e821-3ff0-8ff5-5233c77e54d0 | -9.11442 | -61.27282 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6c03912-a84d-3a52-a926-67717a7b769f | -9.11387 | -61.27631 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 551c0bf2-90c9-33ec-a112-aa954518887d | -9.106 | -61.1386 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9221ded-641f-32f3-af5c-685affac89ef | -9.10443 | -61.25657 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b086800e-50d0-3e19-ae6c-dc71bee258b9 | -9.09162 | -61.16495 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 297c2c8a-6939-335d-875a-6ddb97a45324 | -9.09107 | -61.16845 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ce8b0e9-9e57-3b41-8dfa-3536bab63b88 | -9.08829 | -61.16442 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2333bed0-358f-3778-9018-23f3efcc2f88 | -9.08774 | -61.16792 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60a1c350-26d2-3573-9f9e-ac7739141add | -9.08497 | -61.16389 | 2024-10-12 05:23:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c1c96c86-831e-3e82-a243-59a2b76d6bb0 | -8.34683 | -61.50558 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89b0b855-5128-35bb-80e5-8824f4f939a9 | -8.34406 | -61.50152 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1126148-bb06-39fb-80a0-aa82467abefb | -8.34349 | -61.50504 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8b7c9b4-24b9-305c-968a-a2442a590553 | -8.34016 | -61.50453 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4214cf4-42c9-3414-8142-225151e53325 | -8.22426 | -61.50774 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9250b9b7-d5dc-3648-a0b1-88958aab4404 | -8.22036 | -61.51073 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5735ce7f-f78a-307e-83f7-66caf6479ba8 | -8.07345 | -61.81748 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95a86d67-ee14-3be1-b31a-f0444358441d | -7.9791 | -61.7727 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d48c079d-46e8-3a55-b456-22a4a8814733 | -9.22922 | -62.21099 | 2024-10-12 05:23:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 70d3bc0a-5ea4-362d-8ff3-9bc67e54d519 | -9.15168 | -61.89159 | 2024-10-12 05:23:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58fd9347-f08b-3cb4-adf8-c9cb6fcd0dbc | -8.97308 | -62.37 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cabad49-1103-3d24-92f3-74ca29ae0c62 | -8.97249 | -62.37363 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75ad0110-c90c-3578-b258-8fc3e61be5aa | -8.97087 | -62.36221 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e34480b3-3876-3293-9c79-9d337d321efb | -8.97028 | -62.36583 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c4dad5b-618d-3a7a-9105-0d44c7ee4a1d | -8.9697 | -62.36946 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6474b1d8-6ff6-3cf3-b6df-201895fbda1a | -8.96807 | -62.35804 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2b481fb-fa02-3903-9254-c5600ef6b734 | -8.96749 | -62.36166 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8581bac-1890-344b-993c-1ca1833cb665 | -8.96586 | -62.35025 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cd9da18f-b38b-3087-bdb9-fc02d6b4aa2d | -8.96528 | -62.35387 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40ae62b2-99bb-3486-9d7b-66c65e0e94a5 | -8.96469 | -62.35748 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d0d1161-0be6-3499-ba59-21907f12bb94 | -8.96411 | -62.3611 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34682dc7-d255-3a51-ad66-2a9fd3366004 | -8.96352 | -62.36472 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 066dbc9e-b6d0-39b7-bc57-ecad1fa93347 | -8.96307 | -62.34608 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 78caaa04-29d1-3360-8046-ed0288823a9e | -8.96249 | -62.3497 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02228f9f-01e1-34f8-bc39-db070e2ae74c | -8.9619 | -62.35332 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a04d458-589e-3ff0-8b48-c2b6e471894f | -8.96131 | -62.35693 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f3ac081-64bc-3b24-90ef-f26974e87b8e | -8.96073 | -62.36055 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b15a6131-05b5-3347-9790-84ea1bef7101 | -8.95969 | -62.34553 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 660f768e-7e39-31f5-870b-d314f6c9b1fd | -8.9044 | -62.36254 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 850c0fad-1277-3db6-adc3-5f5724811825 | -8.90382 | -62.36616 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8689942-3aa0-31e1-82ef-d515a0ef0eb5 | -8.90102 | -62.36199 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12425191-fa8d-3542-a41d-e0043dd365b5 | -8.90043 | -62.36561 | 2024-10-12 05:23:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad1d21bf-87d3-3955-a70e-91f34ece19bb | -8.5576 | -62.45316 | 2024-10-12 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 762f74b8-f320-3b64-bffa-d225b6e9f0f0 | -8.55701 | -62.45683 | 2024-10-12 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 931742e0-be12-349d-8ecb-9dc6e7f221a2 | -8.10422 | -61.81879 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14281055-8f67-3330-a217-1f86c69ae42a | -8.6619 | -61.20731 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48d012d2-b1f8-3405-bd9f-7c69703e6f10 | -8.60361 | -61.04073 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5240cfbe-1c3a-3c3d-8e84-9fcfb74aaf7b | -8.60194 | -61.02974 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4bc8aa03-723a-3415-b9fe-972a176dacda | -8.60029 | -61.0402 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dad17b30-eed3-3f47-bcf7-f57a35238f4a | -8.59529 | -61.02868 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84f12a27-8159-3e20-9914-e36521c84f9a | -8.59251 | -61.02466 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a6b7f65-f6f7-30a1-a9fd-3ab7f8e82b84 | -8.59196 | -61.02815 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18a12b08-aa90-3644-95cf-208f0607bd7c | -8.58864 | -61.02762 | 2024-10-12 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd5df57e-84a9-36f4-9436-c317310dc16e | -8.24217 | -61.18762 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f626208c-52ca-365a-b3d8-0a8bc4fd0006 | -8.23883 | -61.1656 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fe234c7-9d77-3e3c-a130-cf8802748ed8 | -8.23772 | -61.17259 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6b0a9c3-8933-3537-babd-f8717f8c9843 | -8.23386 | -61.19704 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fc10d9d-2ad5-3af2-915a-ac1e4ff03c24 | -8.23329 | -61.17904 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 92c79f27-15ab-3390-902c-8cc9ee208786 | -8.23274 | -61.18254 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3426f65d-8410-34bb-a5c8-f0f24b19f730 | -8.23219 | -61.18603 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1770d1e6-80b7-3da3-a8fa-efb6919dac00 | -8.23164 | -61.18953 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ed35400-9cab-3d83-95b5-48ca49d4dec7 | -8.23108 | -61.19301 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db584dc7-5e1e-39f0-b8dd-eb75dc7be0a0 | -8.23107 | -61.17153 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cf932dc-eefe-37b9-aa38-b4b95cd3fd2d | -8.23053 | -61.19651 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4558299-a7ea-30ad-8d4d-1880e6b3827d | -8.22997 | -61.1785 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11530b4f-d36a-3a5c-9cda-e064c6ab1aba | -8.22942 | -61.182 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f3e274b-c7e2-3da4-bc06-1c20cc8bc33c | -8.22886 | -61.1855 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e86de244-3888-32d4-9fcf-965540a8060a | -8.22831 | -61.18899 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88206a00-2ae1-3d5f-a257-ef21e3b6527e | -8.22776 | -61.19248 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e977a3ba-b817-3073-adca-86bb2e148e22 | -8.22721 | -61.19598 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 12b28a7b-3ef3-3e8b-9f45-d1877c4f98aa | -8.22609 | -61.18147 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82fd7e81-dc03-3815-9cee-879b3eb9483f | -8.22554 | -61.18496 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6a9dab47-8b5f-3a7e-b513-6bcfefe778f0 | -8.22499 | -61.18845 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f773389a-1a52-307f-9ce8-326b117f7f0a | -8.22443 | -61.19195 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b28e2a62-4670-392f-ae38-b5a65be64834 | -8.22388 | -61.19544 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e8e3f3e-abce-3108-8365-9326afbacde2 | -8.22276 | -61.18095 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d03f7af-1262-3081-aa9c-dc6f867e8f43 | -8.22221 | -61.18444 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b31db0d5-95fb-3beb-972e-ebc8b4580946 | -8.22166 | -61.18793 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ddc562c7-249d-383e-8fec-7b6a2e6f1113 | -8.22111 | -61.19143 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83adb919-c029-34d5-b3fc-21ff849ce7d4 | -8.21888 | -61.18391 | 2024-10-12 05:23:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README114.md)
