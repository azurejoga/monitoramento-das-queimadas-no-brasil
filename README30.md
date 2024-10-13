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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93a82044-f6fe-3dfa-a0f4-2e8aadcaf866 | -18.2364 | -56.4806 | 2024-10-13 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.8 |
| b094712b-4309-3cc2-ae68-4913bda62eed | -18.2368 | -56.4597 | 2024-10-13 02:16:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.5 |
| d4d4d38f-4ac4-3ce8-b992-f2a6efa70237 | -9.98405 | -64.78941 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 09cd27b2-bf5b-3b5a-ba0d-839a5b349f92 | -9.92166 | -64.77613 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 9f09d33f-b6a0-31c3-ab57-01f9bd057297 | -9.88486 | -64.81094 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 83e27816-7fec-30bb-bcf8-335680dd018e | -9.88271 | -67.28832 | 2024-10-13 02:17:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f38efab8-16dc-30a2-865f-6fa36d2bd2fa | -9.87384 | -67.28962 | 2024-10-13 02:17:00 | TERRA_M-M | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5fd172fb-0b00-3327-bee0-476df27ffae1 | -9.73767 | -64.22884 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 30.7 |
| d4b68365-623a-39fb-90a1-464c13817ed2 | -9.73635 | -64.2358 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 166bc7e8-8cb9-35c7-9cf6-ba0e90e674cd | -9.73586 | -64.21654 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 661a8a9f-7f01-3819-a549-87f95450aa3d | -9.73446 | -64.22352 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ab9f4e01-4ce9-3516-9065-8f8036bdbc47 | -9.7293 | -65.07314 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 597a593d-edd7-3d62-9a5d-b5a56d6fe014 | -9.72768 | -65.06222 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 6b61b1a3-bd0a-380e-9e3f-3f697e200b90 | -9.72745 | -64.23062 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| c9863415-254b-31f5-b992-1aaaed27997d | -9.72562 | -64.21826 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ae1d24b0-af4a-313d-aeee-273d3576502e | -9.71721 | -64.23234 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9bf9c6eb-0306-3c9b-b8a6-3cfb3899c456 | -9.64015 | -64.95797 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d55af22d-56e2-339e-b11c-f0e4840d15ca | -9.63818 | -64.46057 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 56fa6abc-bf3a-304e-af27-eafb9d7cd716 | -9.57205 | -64.29871 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 9d2eaeb4-086a-36db-b725-5793860c2d44 | -9.57019 | -64.28658 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 636ba8d4-4605-3ce6-a0fb-dd68010b94ae | -9.44254 | -66.07112 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3d5b5d5a-3bd5-3a8e-8fc8-d6e0e3542b26 | -9.44114 | -66.06138 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d2a0d135-701c-3a63-948f-79df0c86d479 | -9.40203 | -64.46101 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a5f44968-7a2b-322d-9b0a-f0ac884932d1 | -9.35793 | -65.74903 | 2024-10-13 02:17:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8dfa3dc5-2ace-3d11-bde9-104c1f775734 | -9.31931 | -64.45514 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 947f5102-033b-321f-a20e-7cefc0b4257f | -9.27428 | -64.49306 | 2024-10-13 02:17:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d95bcb79-a079-3628-80ec-b007d55326fb | -8.57275 | -64.04414 | 2024-10-13 02:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c425d8c6-4b19-32f2-b8b2-792b9c3bd615 | -8.23773 | -64.0882 | 2024-10-13 02:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 28.2 |
| ec488856-ad9e-3e13-b037-e00c9fd8475a | -8.23349 | -64.09477 | 2024-10-13 02:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 56217545-1968-33b5-abf1-f3f61df9c3a7 | -8.23155 | -64.08165 | 2024-10-13 02:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 53d9300a-95c3-384a-92f7-ba6c6664a1e5 | -8.03195 | -71.40015 | 2024-10-13 02:17:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0adaca3e-eb7f-332f-bc18-dfd4e0b6ebc4 | -8.00714 | -72.31807 | 2024-10-13 02:17:00 | TERRA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 744c36d0-6c7b-3528-a026-7ab100c90a81 | -7.5065 | -72.70914 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d4e30f60-abe5-3988-9b42-651dc87858e6 | -7.50416 | -72.71572 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9fff6774-a19a-3074-b826-cee7c536aeb5 | -7.37526 | -64.66626 | 2024-10-13 02:17:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| f6a2b4cf-833a-3486-8153-5af2db4cc1b6 | -7.37344 | -64.65388 | 2024-10-13 02:17:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 21c00a36-9aa8-3bb8-bfa8-f21cd897f417 | -7.32636 | -72.64782 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 9a731904-bc5c-3255-827b-0196123ac5ca | -7.32326 | -72.65439 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 01fdf23d-7b51-3a84-8339-e1490e029db4 | -7.32143 | -72.64085 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3ace8247-24f5-3eae-908e-9193c1275f46 | -7.29451 | -64.67228 | 2024-10-13 02:17:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e71d5d5d-4aa9-3c21-9e42-50c16d0be78c | -6.97969 | -71.78041 | 2024-10-13 02:17:00 | TERRA_M-M | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dd88f55a-c2cd-3276-bb4c-31300ea9e14a | -6.97814 | -71.7688 | 2024-10-13 02:17:00 | TERRA_M-M | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| dac9555e-b105-3d37-8772-d72e2e13d4ff | -6.80978 | -64.32536 | 2024-10-13 02:17:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| fd408e21-7c11-3e2f-a7ef-e8531d59a560 | -11.49746 | -65.11603 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0b5419b1-eb53-3730-8b6b-a6b374170fb5 | -11.49593 | -65.10565 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8b8fa575-3ef4-39d3-9916-96267328272d | -11.29584 | -64.99921 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9f714ac4-d643-3111-a870-a963c8b97636 | -10.90385 | -65.10669 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5e2b053f-4d30-3714-b97f-659767d0baeb | -10.89434 | -65.10826 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b8dd424e-1e0d-311f-be00-a8299444397b | -10.85852 | -63.92347 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 18.8 |
| bd05ca66-44b9-397d-9eec-f4f089cd726e | -10.85661 | -63.91078 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 00fab844-2ead-3a8b-8792-2c3cbc0b4ef5 | -10.85469 | -63.89811 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7f615170-a852-3706-b17d-91ffdc1495b9 | -10.78709 | -65.16929 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9bc9879c-fb3c-3f3d-a853-16efba1571d0 | -10.7856 | -65.15912 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5a6c612e-5ed9-34bf-8da0-7dce5c48f312 | -10.74463 | -65.07932 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0e4d7e27-d329-33d9-80e1-2d4979b713d2 | -10.73506 | -65.0808 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 1d559893-a7fc-3d12-adb7-faa83cd17a67 | -10.6969 | -63.46593 | 2024-10-13 02:17:00 | TERRA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 44a85e68-0287-3644-9029-b578e97efbd2 | -10.69387 | -64.12337 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 13c2cf24-be6c-3151-a502-364a4bd8ba8f | -10.69205 | -64.11137 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9c67e685-5b00-3891-9b45-d271b8f304bb | -10.68624 | -63.46767 | 2024-10-13 02:17:00 | TERRA_M-M | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a78f0914-cfe2-3d1f-b0d0-84078732fcfc | -10.63931 | -64.44061 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 908320d9-68e8-3241-9ec9-c18d117767ee | -10.62934 | -64.44205 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| eb27310b-85f0-3dee-9b83-34427293262a | -10.62325 | -65.21143 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b42f9743-efcf-3cfd-a395-3ffbf77b0eef | -10.61945 | -65.21781 | 2024-10-13 02:17:00 | TERRA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ec4c0f42-53b4-3402-8b99-512124aa94e3 | -10.55552 | -64.02616 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7ae725ff-a1e5-3b94-b8e8-d94d0cb4ec6b | -10.49111 | -69.70023 | 2024-10-13 02:17:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 044bea16-416d-3e1e-a3d6-1308ab121d76 | -10.46192 | -69.69424 | 2024-10-13 02:17:00 | TERRA_M-M | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 073926fb-f329-3e2a-8232-6774e4e19c0a | -10.09006 | -64.46766 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| aee26bc6-3c31-39c7-a8e6-5d32ceb6da2a | -10.08005 | -64.46929 | 2024-10-13 02:17:00 | TERRA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7541b325-275f-344c-8fba-38e1d293ac19 | -3.04606 | -61.68872 | 2024-10-13 02:19:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 7d12eebf-9b7b-30dd-83e4-7926908ca745 | -1.733 | -54.173 | 2024-10-13 02:25:16 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| bca31b8a-02c2-315a-a5ec-8b30658af0a1 | -2.1693 | -48.8108 | 2024-10-13 02:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| daa9ca40-ef9c-3783-ba44-a9f10c01c841 | -3.0731 | -54.2473 | 2024-10-13 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| cf5516ce-0024-3a78-b0ad-ec3cb69b5cc3 | -3.0915 | -54.2469 | 2024-10-13 02:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| b9663938-1f0d-363a-aa3e-51b9edde460c | -3.0956 | -53.0559 | 2024-10-13 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.9 |
| ab9f6ab2-a983-3ebe-9c36-9997fc7de4af | -3.0957 | -53.0355 | 2024-10-13 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 165.0 |
| 085adbae-841c-3369-8c3b-88e9c25e3277 | -3.114 | -53.0554 | 2024-10-13 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 10d1d867-9d07-3f15-a5c5-fe73cf1e45bd | -3.1141 | -53.0351 | 2024-10-13 02:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 6ae6ead6-e66d-34cc-87ae-c2d332344a8c | -3.1606 | -50.4766 | 2024-10-13 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 620f65c3-a220-354e-8943-396a267ef84e | -3.1607 | -50.4556 | 2024-10-13 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| dabda533-e74b-3b9d-8dfc-06208c2932fa | -3.1791 | -50.476 | 2024-10-13 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| f64edf18-007a-3bef-9edf-83c65c5e2c00 | -3.1792 | -50.4551 | 2024-10-13 02:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 17e517fa-97fc-3661-95d3-8a8de6f4265c | -3.3594 | -47.3271 | 2024-10-13 02:25:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 00500055-ab6e-37b3-9831-53792df14416 | -3.3595 | -47.3053 | 2024-10-13 02:25:25 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 1b3b3f6a-e4cc-3ad0-9043-10e71a85582b | -4.1148 | -48.2515 | 2024-10-13 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| b0c0ea2e-65e2-31ee-adfa-83f694d1ca6c | -4.1149 | -48.2299 | 2024-10-13 02:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 90253d41-93fc-3781-ba9e-2e90f81875d9 | -4.3985 | -44.4881 | 2024-10-13 02:25:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b1acea8d-6c67-3a4d-84c9-5cbc25b3c2bc | -4.3986 | -44.4652 | 2024-10-13 02:25:31 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 112f208a-6508-3a49-8e95-0f4d35ba3d4c | -5.1381 | -45.3969 | 2024-10-13 02:25:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 324aa6e9-1d16-35ee-a18b-0e1bc9b66bc8 | -6.1301 | -47.2664 | 2024-10-13 02:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 2279e765-6b85-3b9e-84c4-07d1cd1d9cac | -6.3909 | -41.6016 | 2024-10-13 02:25:42 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| b61fb568-93e3-3043-a08c-8e426ea8551a | -7.6627 | -47.3229 | 2024-10-13 02:25:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e098beba-93e1-3e08-8e30-fd9943f93553 | -7.6815 | -47.3213 | 2024-10-13 02:25:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 18d2fd7d-5846-3ba6-b963-5a857ec94685 | -8.6856 | -46.6061 | 2024-10-13 02:25:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| f4b43748-82b1-3452-945e-fff0735e1013 | -8.7045 | -46.6042 | 2024-10-13 02:25:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 2296019a-0033-3593-b667-b8e0914489d8 | -9.7359 | -64.2295 | 2024-10-13 02:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 78786390-2362-3848-9126-0c58370193b3 | -10.5097 | -42.5023 | 2024-10-13 02:26:05 | GOES-16 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 70.7 |
| 44c2f09b-4893-3d37-9bce-18da03d75e73 | -10.5091 | -49.9798 | 2024-10-13 02:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 325.7 |
| 3948088e-cd51-332d-aa58-df58c3522896 | -10.5094 | -49.9584 | 2024-10-13 02:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 333.5 |
| 50186660-0ccc-3e5f-9ec8-44e2c80a9f1e | -10.5281 | -49.9778 | 2024-10-13 02:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 335.2 |
| b1e94ce4-3ccd-3c64-ac5d-a8cb5cb312d5 | -10.5283 | -49.9564 | 2024-10-13 02:26:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 404.2 |


[Clique aqui para ver as próximas entradas](README31.md)
