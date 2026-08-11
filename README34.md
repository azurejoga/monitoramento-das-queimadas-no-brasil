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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b239fd8-4ea4-3f4e-a90d-8a6d6726a658 | -13.5502 | -46.2844 | 2026-08-11 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 5b2417dc-9fea-3c13-9168-8c9e8ce03514 | -11.0294 | -45.6536 | 2026-08-11 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 187.0 |
| 3c628ebb-0101-3c2a-9144-6ef6541e7dd8 | -8.9602 | -60.4973 | 2026-08-11 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| e8ebdf30-8749-33d0-93f1-b751b617fb5c | -8.96 | -60.5358 | 2026-08-11 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| b55f073c-dc69-307f-a6f7-b580d837dabe | -13.8611 | -53.7845 | 2026-08-11 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 0c92c508-3574-323d-be1f-8bd4fa5d98d5 | -13.8608 | -53.8053 | 2026-08-11 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| bdc89068-1b7a-3f8e-8c3b-7ee28eb81057 | -11.7908 | -51.8189 | 2026-08-11 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 329.2 |
| b549d9e0-4c3e-372d-82d2-8167635af969 | -13.8419 | -53.7867 | 2026-08-11 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4ef67a2c-675f-3832-b151-b7e05fbfc1eb | -11.886 | -48.0766 | 2026-08-11 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 4c7461d0-740e-3739-8f4d-cf57f455c0b1 | -10.2271 | -45.8708 | 2026-08-11 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 338.0 |
| e22b0757-e004-3927-ab70-4dc6304f46d6 | -13.5498 | -46.3074 | 2026-08-11 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 227.7 |
| f13b1e05-1e74-395d-ab09-b2a76d9a3e23 | -11.7905 | -51.84 | 2026-08-11 14:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 396.6 |
| 2402c6b6-1496-32e9-99dc-17563d566c6e | -13.8204 | -53.9347 | 2026-08-11 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 6988097d-e70e-3fe4-8c9a-0678cbc303b3 | -14.4265 | -52.1376 | 2026-08-11 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.1 |
| ab7f0c3e-c7f3-3e4a-811c-c97ac485eb7c | -8.9415 | -60.5174 | 2026-08-11 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1da1f8cb-03de-3689-a205-e98afc7e9e13 | -15.0736 | -52.7309 | 2026-08-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| f2700621-c881-36e9-95dd-1ecc860002c8 | -14.2877 | -45.2835 | 2026-08-11 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 40cec828-675c-3231-807d-eac7dc304bc4 | -15.0541 | -52.7335 | 2026-08-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 2e39784a-af90-3b0e-adeb-4c731dd6ffbd | -7.3868 | -45.1098 | 2026-08-11 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| e1575048-7473-3d09-8952-e2fae3af94db | -8.9601 | -60.5165 | 2026-08-11 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1a155e79-fdb2-3ccf-bb42-b325827ed9ee | -9.3717 | -47.4897 | 2026-08-11 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5c7ace23-2d55-3f10-bb5e-4a623bf04638 | -15.0739 | -52.7097 | 2026-08-11 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| f9f41cb1-7dd7-32c6-964d-edc0847ea86a | -10.2275 | -45.8481 | 2026-08-11 14:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| e667d584-413d-3a9b-bd4e-ab4ae35834be | -11.8669 | -48.0791 | 2026-08-11 14:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| d9bcf37a-a054-3b3b-8ef1-58997f7ab294 | -8.9598 | -60.555 | 2026-08-11 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 8f9bdcb4-9d24-349a-931c-3c0cdc841ebf | -14.2559 | -51.9686 | 2026-08-11 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 9404c45e-0e18-3e2f-8083-8773f965cff4 | -15.0739 | -52.7097 | 2026-08-11 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 6d9c0c4d-ab99-3c60-951f-e34d0ac7961e | -9.3645 | -48.0404 | 2026-08-11 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1308.4 |
| 0a2dd5fa-4707-3dcc-916d-649d73264d09 | -8.9601 | -60.5165 | 2026-08-11 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f739cb32-c094-3d13-ab2f-f22ebc1e0ff9 | -13.88 | -53.8031 | 2026-08-11 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 941efbad-83a3-337f-a11f-eb486881879a | -9.372 | -47.4676 | 2026-08-11 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 0251ee4b-00bb-3e31-a491-1eab75933197 | -13.8803 | -53.7823 | 2026-08-11 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 8fce8f0f-bd9c-3d39-a496-965f6b8a25b3 | -13.8419 | -53.7867 | 2026-08-11 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 1eefa107-9407-3fc7-ad8e-fef0adf4b321 | -11.7908 | -51.8189 | 2026-08-11 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 314.3 |
| c665ef48-03f8-3030-aa70-97b10c0a6e31 | -14.2559 | -51.9686 | 2026-08-11 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 305.0 |
| 7283f14c-0209-3e06-b85f-5d739abcfae9 | -15.0732 | -52.7521 | 2026-08-11 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 8cb69e53-4c16-3c55-a1ce-7a5c5df561a5 | -11.8669 | -48.0791 | 2026-08-11 14:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 8df628e4-6d19-35bf-844e-08e7bba2cb20 | -15.0541 | -52.7335 | 2026-08-11 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 5d177320-88d2-30f1-a4c6-1404db166785 | -9.3717 | -47.4897 | 2026-08-11 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 230.3 |
| af7962d8-e8a7-32d3-ad4a-0b73083dd32d | -8.96 | -60.5358 | 2026-08-11 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 270dcaef-f64d-3f8d-864f-7a0ca595538a | -13.5502 | -46.2844 | 2026-08-11 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 149.6 |
| 9a3f2c88-e98e-3d16-a5f4-96b84eac6c45 | -11.0294 | -45.6536 | 2026-08-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 389.2 |
| 1a6036b1-d1e0-3c93-a02f-21ebb1f8c68f | -14.4265 | -52.1376 | 2026-08-11 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ad46ca8c-1ccd-3318-aa19-e9fff5bc6826 | -15.0736 | -52.7309 | 2026-08-11 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 603b2b84-02bb-32cd-8e4a-a2d163a59b8f | -9.3648 | -48.0185 | 2026-08-11 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 191.7 |
| 042b3343-3b01-3c6c-8870-b93be431d402 | -8.9416 | -60.4982 | 2026-08-11 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 9779d81d-a943-3e35-b78d-864d8c32761d | -9.3714 | -47.5119 | 2026-08-11 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 254737ac-f5d5-3030-af5b-a360323fd094 | -15.0545 | -52.7122 | 2026-08-11 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4f82cb3b-a681-325c-824f-b2ba463c0e94 | -14.2877 | -45.2835 | 2026-08-11 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 7f65398a-3242-3657-a28f-e3c2f3765c58 | -13.8611 | -53.7845 | 2026-08-11 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 0ad9561b-0dd0-33a4-a192-684bb461789a | -13.8608 | -53.8053 | 2026-08-11 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 113.8 |
| 8bb99062-63ea-3eb2-99e7-89cb5e67ffe7 | -15.0728 | -52.7733 | 2026-08-11 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 0978b305-2f20-3d35-9251-83cbfba7e6bc | -11.0298 | -45.6308 | 2026-08-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 231.8 |
| b03aeacb-2583-337f-a2ea-b12bfaf0aed6 | -11.7905 | -51.84 | 2026-08-11 14:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 379.3 |
| 1f2fc727-2765-3bad-a801-c9096c5d8630 | -13.5498 | -46.3074 | 2026-08-11 14:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 337.2 |
| 4b9fcefe-b1c3-3593-bf03-c0335eccc512 | -11.0107 | -45.6333 | 2026-08-11 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 500.0 |
| 8ab42366-db20-3d67-a856-b4463a4df4e6 | -8.9414 | -60.5367 | 2026-08-11 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c23128f8-529e-3632-934d-546827774e48 | -8.9602 | -60.4973 | 2026-08-11 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 5d5f0260-d154-3a05-945a-32e72e344c77 | -14.25 | -52.0 | 2026-08-11 14:15:00 | MSG-03 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 61623fc6-5487-36c4-ba9b-f5fe5ffa90b7 | -9.38 | -48.08 | 2026-08-11 14:15:00 | MSG-03 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7468832c-25b8-34f7-a8eb-095a216b9ffb | -9.38 | -48.03 | 2026-08-11 14:15:00 | MSG-03 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e957eb00-ebca-36b5-ad37-eef1f03c27e5 | -9.35 | -48.07 | 2026-08-11 14:15:00 | MSG-03 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55a8103d-bf86-3d2b-9251-cc3506cfbe07 | -14.2559 | -51.9686 | 2026-08-11 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 304.3 |
| a6c40c07-0709-3322-ac96-bfaa2df6c7cc | -8.96 | -60.5358 | 2026-08-11 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| c8104734-b00f-39f1-aed0-dccc2372f21e | -15.0541 | -52.7335 | 2026-08-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 136.2 |
| c8105dc3-1c9c-3b04-8af1-9c991e75d5a1 | -8.9596 | -60.5934 | 2026-08-11 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 75017550-31fb-3bcb-9227-0b3981f732a0 | -9.372 | -47.4676 | 2026-08-11 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| a3246b27-5525-39fd-955f-a51079e4dfca | -13.8204 | -53.9347 | 2026-08-11 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| a4cf8e10-bcea-3cda-b63d-fe1d1d8994ea | -15.0545 | -52.7122 | 2026-08-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 10586950-8514-3bc3-bd86-a58a0bd81dc1 | -14.2551 | -52.0112 | 2026-08-11 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 4d876452-8388-3a33-81fc-26b2530e15a4 | -15.0736 | -52.7309 | 2026-08-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 8817a0e5-a032-3d57-bb52-eed08272584d | -13.5502 | -46.2844 | 2026-08-11 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 151.8 |
| 8dd4738e-3c6d-3a58-a169-414e13c8ce66 | -11.7908 | -51.8189 | 2026-08-11 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 4b52a712-22bc-3bcd-95ef-7dce28ed2fd5 | -13.5498 | -46.3074 | 2026-08-11 14:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 296.5 |
| d04a359c-ce0b-34c8-864c-3ebf79856333 | -15.0549 | -52.691 | 2026-08-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 2c87b566-c197-355e-abe8-394cf1838854 | -13.8211 | -53.8931 | 2026-08-11 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 108.2 |
| aca16424-13dd-3b77-bac5-540f791301a6 | -8.9415 | -60.5174 | 2026-08-11 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d22e3e6f-1053-3a4a-a4fa-a2f5843092e7 | -11.8669 | -48.0791 | 2026-08-11 14:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 5ec8d880-9466-3e4a-b66f-a3be472adec3 | -13.8403 | -53.8909 | 2026-08-11 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d3bfcac8-42e8-392b-b6d8-85b3121a1308 | -14.2877 | -45.2835 | 2026-08-11 14:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 87b87936-20cb-3712-b2aa-0fa091ad0e52 | -11.7905 | -51.84 | 2026-08-11 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 0120d5bf-a15f-3650-a98e-b807e08e790c | -10.2271 | -45.8708 | 2026-08-11 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 744.0 |
| 3086c57a-5dcb-359d-bbff-edc71b911cbe | -13.84 | -53.9117 | 2026-08-11 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 824585f0-3721-3eed-8582-c0a3ffaf7e04 | -10.2275 | -45.8481 | 2026-08-11 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ca81efb7-18f8-321c-9721-1d5c56235979 | -10.2268 | -45.8935 | 2026-08-11 14:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 645.2 |
| 5f4436c7-eba9-3c32-8716-9e21e88bf48d | -15.0739 | -52.7097 | 2026-08-11 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 10925b33-919d-3f10-932d-14d960d9dace | -9.3717 | -47.4897 | 2026-08-11 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 91cc40f1-ce9a-3e2c-b2dd-335bae291ce0 | -14.4265 | -52.1376 | 2026-08-11 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| d6ec81b7-a3ec-3683-947e-6bc2f4abf09d | -8.9601 | -60.5165 | 2026-08-11 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| f96d8cbc-2f4a-3a7e-b4fe-728086997aba | -11.0298 | -45.6308 | 2026-08-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 32623c66-f3bb-3700-a8f9-0ca5dbb82788 | -11.0107 | -45.6333 | 2026-08-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 333.5 |
| ed6cd269-fb4a-3911-b035-140e6608dd5c | -11.0294 | -45.6536 | 2026-08-11 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.0 |
| 6c48fa54-635c-3d58-a981-d93d60e96837 | -8.9416 | -60.4982 | 2026-08-11 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a28f451e-5867-30f7-8249-8dc2b7aa7219 | -8.9602 | -60.4973 | 2026-08-11 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 0ed7a030-c1fd-3282-b79c-ffed324fb15b | -8.9598 | -60.555 | 2026-08-11 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a31b8579-5b3f-3653-a5b9-dea135d164b6 | -13.5502 | -46.2844 | 2026-08-11 14:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 87183905-bacd-3700-b4a7-471ab18d3ec3 | -15.0739 | -52.7097 | 2026-08-11 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 768dad08-31ca-390d-a289-24ede65bcc7f | -11.0298 | -45.6308 | 2026-08-11 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.4 |
| dc58ae8e-ba5f-3904-8e3d-cccb4ff8569b | -15.0549 | -52.691 | 2026-08-11 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 120.1 |
| feb9dcd1-81a9-3d00-9126-93a7f73cc72b | -14.4265 | -52.1376 | 2026-08-11 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 132.6 |


[Clique aqui para ver as próximas entradas](README35.md)
