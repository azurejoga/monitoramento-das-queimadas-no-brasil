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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fc2d985-e53b-3e8a-81b4-4b4497536e11 | -3.04162 | -53.87865 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f301ab1a-a002-307c-90a6-bbd4505e3687 | -6.24149 | -53.15681 | 2026-10-02 05:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a22688a-9120-3ec8-8165-06bfd8b3b367 | -2.9027 | -54.14823 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e6d31ef-0a00-353f-a53b-5c60ca1f92da | -4.38322 | -54.83104 | 2026-10-02 05:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 07c03a50-33af-3d88-9109-3f8879baa520 | -2.89622 | -54.14722 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a033b05-19d4-3ec8-ad8b-ef7289678b4e | -3.29835 | -53.85107 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 12c720de-cd01-30cb-b57c-11e458b2ba11 | -2.89626 | -54.14449 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ca9ddb6-b979-3f1e-848b-f9a7a8696f5a | -3.02021 | -53.97887 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 78f23d13-b4a2-323a-93d0-1bf09ef83695 | -3.13677 | -53.74057 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 263187f3-81e6-3d01-a184-76612d72e760 | -5.86017 | -53.47985 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 91bff7d1-767d-307b-8b61-c2463df04ef6 | -3.00924 | -53.2346 | 2026-10-02 05:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e3c43c8-3d35-3e2d-81cb-4cc1ba80e3f4 | -3.13367 | -53.74251 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 5060957b-914d-3de3-8397-30ce62d97f1d | -3.14168 | -53.75315 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 919c54c5-748c-32bf-b82e-7b34f9e22cea | -3.29172 | -53.85003 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d1da3972-e384-3cf8-be00-521415e12883 | -3.00862 | -53.88733 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4e4a91b4-ca20-333e-a364-1088fbd7cfca | -3.01435 | -53.89399 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 406e796e-1dae-3b94-abe1-337de5e259d3 | -3.29002 | -53.86153 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e85315e4-7966-3e68-978a-ef92a252e5e9 | -3.17615 | -54.09536 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| de288acb-76fb-3c19-a31e-764662eb91d9 | -3.01553 | -53.23344 | 2026-10-02 05:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 377483d7-85c5-35be-9df7-203be9a6a36f | -5.89359 | -53.49669 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6050243-8444-3299-96f4-b65e223512a2 | -3.12747 | -53.75709 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a6d902cd-3b4c-3951-a5c1-2e22ed02f20b | -6.10189 | -55.68274 | 2026-10-02 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 709df7fc-5875-320d-9b95-d55dc76c0d7d | -3.17129 | -54.08327 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d654ada4-bc40-3f6d-b68d-a357024498df | -2.89728 | -54.0948 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8c3b992-48c8-3420-be8e-4a25de615788 | 4.69514 | -60.85507 | 2026-10-02 05:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 002b909b-b7b0-3197-babd-3deb76c65561 | -5.84575 | -53.48076 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6cd8eb6-b9fa-3064-b34c-56f8b9dd11d5 | -5.99869 | -53.55248 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9cb922f1-be25-38ae-a70c-b05d6ab25493 | -5.85947 | -53.48502 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0016c0b7-296a-3daa-9601-9f555091af0e | -5.87154 | -53.5013 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c91d1e3a-16ed-3d21-bd19-d99ebc75b030 | -5.00515 | -56.28565 | 2026-10-02 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52d10a73-915c-34a2-8834-8111c853846e | -3.17358 | -54.10752 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d38e8aec-3170-30b1-a660-7e25017982db | -3.00202 | -53.88636 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 960275db-1588-3b86-9336-ba0092b93895 | -3.13501 | -53.75221 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1776be2e-0950-33f4-8a69-9c9a9bfe36ba | -3.01931 | -53.89292 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 205f8764-e016-39e0-87f9-8e23c7858425 | -3.8478 | -55.80983 | 2026-10-02 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f3db1ff-b29c-3878-9cc2-26d08626c90b | -3.17214 | -54.07761 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 11a011b3-f67d-31c0-8e63-40157ad48d5c | -3.00116 | -53.87854 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91a457b1-ec10-3040-8584-cbedf0bb6485 | -5.99957 | -53.54607 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b48e927d-4078-3158-a59c-44db04e9c8da | -3.28594 | -53.84325 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| fc8d62af-4b18-3c16-bde6-193f71002aef | -6.24256 | -53.14881 | 2026-10-02 05:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f8bc706-7e2d-3a9c-8145-89b72b2a5cd8 | 2.00909 | -61.08568 | 2026-10-02 05:53:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d11c6fb5-f502-3b99-a388-5a7f6bac30fd | -4.68412 | -55.79633 | 2026-10-02 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3fc8f8e-afb4-3e26-add0-22b62ac2ad20 | -3.18105 | -54.10718 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eccc23d9-10ee-3bc7-a6db-76cdfd8d9006 | -3.28425 | -53.85473 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb7b86f0-2e93-3dfe-9e06-aac18e47b418 | -2.87625 | -54.88228 | 2026-10-02 05:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a7c0a3b-84f1-3305-b952-d4a23c72af1d | -3.13866 | -53.75512 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ca8bff7d-e3ac-3eee-af55-25c8ccaa46c1 | -2.89812 | -54.08937 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6549a7c9-410e-36d6-b3ce-e0e5987153b2 | -4.38959 | -54.83178 | 2026-10-02 05:53:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34987443-798c-3529-9916-7211eb86a676 | -5.89982 | -53.50333 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18b6376e-e4e5-38ac-bede-2f327c0824c5 | -3.16561 | -54.07661 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1222979e-ee85-39ed-a344-a709d41919fd | -3.00776 | -53.87954 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00c7ccca-15a7-3947-a9cd-2a4ed979b369 | -3.16794 | -54.10563 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1cd14904-b083-34e2-88fc-204b8e38a302 | -3.14034 | -53.74349 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c0fc0bda-60ab-3d2f-bc75-3383a4fe339d | -6.23544 | -53.14742 | 2026-10-02 05:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3034b4f6-59e4-312f-921a-b38256727ac5 | -3.15742 | -54.0867 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f92660a-d99b-3f08-a9fd-7d66abf67885 | -6.2436 | -53.14109 | 2026-10-02 05:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e0de0d1-f5c4-3958-a0b6-5d96c52a97cc | -3.16878 | -54.10004 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f74b3e9-3c5b-391c-9f2a-7acd96cd3547 | -5.89263 | -53.50366 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 499d9f06-29e7-327f-8804-8cdea9aaef31 | -3.02103 | -53.97328 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 575b2d36-299c-3a19-810d-5f0a2e9d1a21 | -6.23643 | -53.14004 | 2026-10-02 05:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b5fbf355-459e-34c6-938b-5e9fbe25b847 | -3.132 | -53.75415 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a168d1bd-ad65-3596-9909-d7f1d2e82b8a | -3.18755 | -54.10308 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8935211e-0e91-3dd7-9b47-c29eb8f536a1 | -6.00559 | -53.54104 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2121b2c9-f38a-343f-9417-1006a8cd4fa7 | 4.69215 | -60.86002 | 2026-10-02 05:53:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e0fdb2f-81c0-3a5e-bef7-1f5d3dba3a02 | -3.18174 | -54.09711 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 707c291e-547f-31c4-937e-34edb2c3201c | -3.13284 | -53.74833 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c0074fdc-5a67-3482-9d52-24f03ac75b50 | -3.01614 | -53.23537 | 2026-10-02 05:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e0c764d-6386-384c-be11-1638ed7bdab6 | -3.12834 | -53.75126 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 425691d9-0d13-3320-999d-ff862c2503f1 | -3.2834 | -53.8605 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b850fc4-5150-33c9-9592-22344539b084 | -5.99786 | -53.5456 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5bc1ca5b-8795-369d-ad65-ee281ca332a7 | -6.00645 | -53.54794 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| bb6e8e8e-6acf-3115-afa9-107b5d63edd0 | -3.00289 | -53.88064 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 525c3a45-9614-30f1-90b6-6b5f4a9fd65e | -5.26873 | -56.05225 | 2026-10-02 05:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d91f429f-b40d-3c6a-89a0-da1b51422e54 | -3.2975 | -53.8568 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b68c0022-d06d-37d1-af2a-7361905251ac | -3.18763 | -54.10778 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4654373-2987-3be7-9ed0-3cacbf83ae5d | -6.07564 | -53.30801 | 2026-10-02 05:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed2ad501-9c29-363e-a196-f73e1dc58cf2 | -3.02301 | -53.96945 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b2db4000-d7c1-339e-a4cc-f48cc0f2d4f4 | -3.1819 | -54.10154 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8ae43583-e661-3605-b1f9-89b0510f69f0 | -3.16477 | -54.08221 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2a508583-70e1-3b56-b938-adfc31db9be4 | -3.18014 | -54.1083 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5e92b599-f1e8-3a8c-ad0f-a7ebd6dd9373 | -2.89543 | -54.15262 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 67e78f8e-4cdf-3fce-ad09-5b0b5fbcd088 | -3.29257 | -53.8443 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f96526f4-bc1b-3ecb-9208-f1c6d4bf819f | -3.1867 | -54.10899 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f08c3028-3eec-3454-95df-a454b485d0c4 | -2.89054 | -54.1408 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e51fe56f-c18b-30d0-80fd-94239cb3ad7e | -2.875 | -54.8817 | 2026-10-02 05:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3d39930-3bbe-349e-b9db-38d2fed5e771 | -3.84844 | -55.80548 | 2026-10-02 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1680bc23-5497-33cf-8880-36f3754b0401 | -2.89143 | -54.13279 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f4f5d0c-9bbd-3c68-b363-27662781547d | -2.88247 | -54.88306 | 2026-10-02 05:53:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 14e6d12e-aae5-3c78-a354-f2d29b73907b | -2.88899 | -54.14865 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac025dc5-1b4e-35dd-8a14-65c853ec05b1 | -3.1395 | -53.74931 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e61b646c-a544-37d4-9a96-9f8c4ed7e960 | -2.88977 | -54.14605 | 2026-10-02 05:53:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fa006a5-e938-3ae5-a19a-eb00290f10f1 | -5.899 | -53.49799 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 971ea6c5-7778-3605-b98f-7a6e7e8912be | -5.99703 | -53.55196 | 2026-10-02 05:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 558da063-64e5-3681-9094-a5d710c08ae1 | -3.01522 | -53.88828 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d081cc24-78a1-37a7-9462-dd696e152ebb | -3.00774 | -53.23857 | 2026-10-02 05:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d594f3c9-3530-34df-be69-a6324ff2c942 | -3.17517 | -54.0964 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f10d1cc-0913-3518-b639-60cc5eb7229d | -3.14256 | -53.74735 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b7869edc-d799-3801-90b2-83c88d99f3c9 | -3.00611 | -53.89094 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb85ba5e-fc70-33db-b071-8e4329cf52d3 | -3.00034 | -53.88427 | 2026-10-02 05:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 311babbe-2b83-3b86-b6fd-98807c9a108c | -7.48536 | -55.00612 | 2026-10-02 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README81.md)
