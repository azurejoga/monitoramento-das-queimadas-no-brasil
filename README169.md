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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ac610fe-590e-3154-8af9-38df44e1c069 | -8.4772 | -62.70177 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31a29e28-9112-3c27-8a9c-c84a87ae6937 | -8.47668 | -62.72752 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c6898bf-4a6f-3fd0-9763-48a6b8b71d03 | -8.47148 | -62.64915 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa991468-b6b2-3b98-9452-90b1d2889581 | -8.4694 | -62.73008 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c1e9981-de84-311c-b0e7-dace96e17ae2 | -8.46825 | -62.71516 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95b5f727-c959-3fd4-9d7e-b300fc81f2c4 | -8.46714 | -62.72237 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fac6252d-5220-37ec-a35b-f521b0a36c46 | -8.46659 | -62.72596 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab42f9dc-a5ac-3778-96a1-37c8bc2b0116 | -8.46433 | -62.71824 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1465418f-cce5-3f27-b367-11ea01f16438 | -8.46418 | -62.65173 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b5e54cf-4546-3d45-8b05-3be4272827c1 | -8.46152 | -62.71411 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0bade6c-c1bc-3a56-af3c-575bcccb441f | -8.46097 | -62.71771 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fe6e5dce-f3da-30b2-893a-18ab60e8b90c | -8.45705 | -62.72079 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 416bfe85-a2d4-34ca-b5cb-1b212cf21ed0 | -8.36486 | -62.65946 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 026117ca-406e-334f-8ce1-2e5f4a28cbae | -8.36149 | -62.65894 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db1899af-5088-3ce1-8c49-b5488e53ca32 | -8.80977 | -63.00653 | 2024-10-02 05:33:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 88029ead-59f2-3b91-a031-a4849194cb65 | -8.80809 | -64.06963 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9b630aa0-f94f-3b71-984c-ac13d7c375b4 | -8.70069 | -62.81733 | 2024-10-02 05:33:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e661a47c-ed54-3ac7-9fe6-b075fa52eac9 | -8.69733 | -62.81681 | 2024-10-02 05:33:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c39f1336-1735-345f-8daf-ee0fcc323f02 | -8.69396 | -62.81628 | 2024-10-02 05:33:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ec3a109-1c7b-355d-a131-f5bef7469ee6 | -8.64403 | -63.81591 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd0d099a-c759-3632-886f-c3bc5f26d91e | -8.59544 | -63.34268 | 2024-10-02 05:33:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84cb4e05-e117-370c-96e2-222f2486cbf8 | -8.58018 | -63.4409 | 2024-10-02 05:33:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4737c8e5-5eb0-38a3-a4a3-d56aa321f1b0 | -8.49267 | -62.55591 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9d8170c1-5e8f-3c57-a87b-8a9b8a8d7179 | -8.49051 | -64.05833 | 2024-10-02 05:33:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d229d16-9d52-307a-be21-a809c932b2d5 | -8.49011 | -62.70747 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0f1ac7d-43cd-3f44-baec-b467ef5a02d2 | -8.48674 | -62.70695 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11ae38e9-be01-3b8e-893f-4efb624b805b | -8.48393 | -62.70282 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7aa16b4c-5c91-30b9-8fea-06226a019ce0 | -8.48337 | -62.70643 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 162a4608-aa2b-367b-a30f-997d98dfe81d | -8.48282 | -62.71004 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b43fc6b8-5f73-3741-9fc7-dadb12ac4209 | -8.47609 | -62.70899 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5f56aff-f661-39f2-b362-534a540d1227 | -8.47553 | -62.7126 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 975bddc9-53b1-37e1-8cc0-e4f122080b77 | -8.47387 | -62.7234 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3c273a3-273d-358a-a9e6-e9e39598b024 | -8.47383 | -62.70125 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5a3d032-eae0-373b-b41e-dc743b72a8fd | -8.47332 | -62.727 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4afda6c9-7614-371e-b26a-15d03ed6facc | -8.47106 | -62.71928 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0d0ed97-6867-3743-84d8-e7ebdae9a612 | -8.47051 | -62.72289 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd4e521c-0b32-3a1d-8aa5-a6d20514c57c | -8.46995 | -62.72648 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8304e3a9-3f12-3180-9e33-fce48c0621af | -8.46769 | -62.71876 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51bf375c-c21e-35c9-9bd6-b1599d2d9109 | -8.46488 | -62.71463 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fb5e962-fce3-33a5-a6a0-a025e030a267 | -8.46473 | -62.64811 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 379b4d1d-0037-3c5e-bce3-34362cc1a540 | -8.46378 | -62.72184 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3420f8fb-f5ee-3137-bfd6-205834c0e5d0 | -8.46363 | -62.65533 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05114426-e073-3df4-bc18-0c0ce735f0dc | -8.46041 | -62.72132 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 880d08f2-d0dd-38d2-8a55-4625477892e7 | -8.46026 | -62.65482 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f92ee868-1444-3102-afad-b82463e929c6 | -8.4576 | -62.71719 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d5aa4c72-21fe-39d7-8fed-fade080610ad | -8.36204 | -62.65533 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c14c01ff-1af9-32cb-a3e9-318d62fb6c49 | -9.27204 | -63.33632 | 2024-10-02 05:33:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 911fec1a-8ed3-3ff9-bde9-e1b09aa48182 | -9.25361 | -63.62948 | 2024-10-02 05:33:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 134c1e0d-037e-3c60-b585-fa4b74355a5d | -9.28339 | -63.83139 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86fd69e4-ce2f-34e0-8099-df2f86eccdd6 | -9.2687 | -63.3358 | 2024-10-02 05:33:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3e49577-ab20-39d2-8248-81839a5509fa | -9.25307 | -63.63298 | 2024-10-02 05:33:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11e25b4f-f26a-3f2d-b158-0e4743b04e43 | -8.97496 | -63.93567 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f618f9e-918c-30c0-99c4-c5c118f52935 | -8.91824 | -63.97305 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e37f05a3-9663-3744-840c-f1218346820f | -9.96531 | -62.99938 | 2024-10-02 05:33:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e5890871-69cd-3a70-a6b3-f347ba911c0e | -9.96249 | -62.99526 | 2024-10-02 05:33:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3450b276-d676-3398-934b-216e88f8ebbd | -9.96194 | -62.99888 | 2024-10-02 05:33:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30cb34f4-9e58-3af7-9e7c-03505611c788 | -9.95857 | -62.99834 | 2024-10-02 05:33:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ac662fb-f775-310a-b9fd-829a6bc7ba2e | -9.65192 | -63.42437 | 2024-10-02 05:33:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97c3601d-45f6-3842-b47d-5b3f13d0e2f6 | -9.64525 | -63.42333 | 2024-10-02 05:33:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 609cbe7e-92a7-37cc-ba36-16729c86a539 | -9.543 | -62.80849 | 2024-10-02 05:33:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09477011-41c0-3817-a603-7d048ee3da7f | -9.51064 | -63.19828 | 2024-10-02 05:33:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 257cbd94-f142-355f-bd0e-6e1455b67560 | -9.47423 | -63.36741 | 2024-10-02 05:33:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4b1d1e6-0b42-3404-bfad-cc1573f7d7e4 | -9.35676 | -63.7958 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16810f08-d040-35fb-b0d3-8003c30c65c5 | -9.35621 | -63.79932 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9243f73d-7d35-3f8a-8104-b666fca0c15b | -9.82657 | -64.04916 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7af3fb6-8252-38d4-b602-7e305e72045b | -9.77894 | -63.14861 | 2024-10-02 05:33:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1f7ce822-c8f8-38f2-b825-c34c845c539f | -9.77614 | -63.93732 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a131a876-39fc-3fe4-b22d-aba8c4cca439 | -9.7756 | -63.94082 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0c018d3-48fc-3a16-a99a-dd75cd81fc1f | -9.77228 | -63.9403 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 971c200c-fd9f-384b-a554-5104f37948db | -9.73147 | -63.9846 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a48922e-0f4b-3844-a94b-8f8b0cb02855 | -9.67721 | -63.56953 | 2024-10-02 05:33:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f927808-bd6e-31e2-9597-a79fedbc3a8f | -9.64859 | -63.42385 | 2024-10-02 05:33:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b2aa480-4b1b-3b0e-94af-0a4713a3dd64 | -9.56631 | -64.25816 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea6a4318-d397-316c-8d30-2049e56d18ca | -9.56577 | -64.26164 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4276da3-f63e-3aac-bbad-cbb707e60e3d | -9.56301 | -64.25764 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0e4e703-d9f3-3c8e-9e58-f1eacc689d0f | -9.56246 | -64.26112 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ca8ac30-879e-32f0-9186-e64d39380de0 | -9.56191 | -64.2646 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75d5128c-a99f-36db-8eb2-2feba7195f93 | -9.5597 | -64.25711 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f14a09e9-76c0-3da7-98fa-d53f62345cef | -9.55915 | -64.26059 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df8e7eac-0848-33a8-876b-3aab9ecde96a | -9.55861 | -64.26407 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 847a1f97-1fc2-3dff-8ce4-e83a97dc4b96 | -9.55584 | -64.26006 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb7e82da-b15d-3c85-8364-d4256b731b8d | -9.55254 | -64.25954 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aefa408e-9d25-3102-b4f3-3d27717b88c9 | -9.54923 | -64.25901 | 2024-10-02 05:33:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 05bb4ea5-a165-3814-9902-5d1b1924746a | -9.54638 | -62.80901 | 2024-10-02 05:33:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d503e481-b21f-385e-9807-92700bb0bd7f | -10.05578 | -64.40797 | 2024-10-02 05:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74754bc9-3b18-3be6-825a-f83c81a569c0 | -10.05524 | -64.41145 | 2024-10-02 05:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4807af6d-6140-3bc7-9733-01cfc03c45da | -10.05248 | -64.40743 | 2024-10-02 05:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc649c3b-68ab-3979-b08a-856243fa02e8 | -10.05193 | -64.41093 | 2024-10-02 05:33:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a9a256e-3a59-36fa-b463-5ef1420bf1b8 | -10.00399 | -63.18657 | 2024-10-02 05:33:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feb9acdd-4c90-3fa8-a625-f482f9ca808c | -11.52391 | -65.09279 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 025245c9-6c64-38b6-bff4-db1e1b720362 | -11.52335 | -65.09629 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f9e966b-1212-345d-aa09-823123852fab | -11.28841 | -65.2706 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59951c48-f0e9-3e99-b587-18a069ff7cba | -11.28784 | -65.27412 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfcf3a18-d898-32d6-914f-1c4874b5b101 | -11.2872 | -65.00024 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9156ad0b-8636-32e6-8534-496ef8c12f2a | -11.28509 | -65.27005 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e2f4502f-ff85-3ad1-b131-c58d8c21449d | -11.28453 | -65.27358 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a8e783d8-5cc3-37b4-97bd-23d532a38e21 | -11.26788 | -65.01508 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 396e8e55-c33a-3986-87f6-724cd941abbf | -11.26457 | -65.01454 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd94b633-cea4-3e17-ac64-2a88980585c2 | -11.26402 | -65.01805 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3192501b-bc07-3a72-b945-e05ec44e9a4e | -11.26297 | -64.91719 | 2024-10-02 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README170.md)
