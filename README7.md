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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bee7786f-c439-3c73-a730-d8523bb215d1 | -2.1916 | -50.457802 | 2024-10-21 00:39:17 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 284c67c6-fc96-3836-87c8-fd0872646d76 | -2.1803 | -50.453201 | 2024-10-21 00:39:18 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e16e7cb-5f59-3735-a1e1-2fbfd5eecafa | -2.1818 | -50.459999 | 2024-10-21 00:39:18 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7459930-fa1c-3de3-8cd3-9040f63ded42 | -2.1834 | -50.466801 | 2024-10-21 00:39:18 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72f8a72f-8fff-34cc-bf8f-7804a7954d9e | -2.8121 | -53.315701 | 2024-10-21 00:39:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5770088b-91ad-35c9-8c19-50529a89ed81 | -2.8139 | -53.323898 | 2024-10-21 00:39:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 626bef4d-fc40-38fb-bf94-58864cefc9f4 | -2.8157 | -53.332199 | 2024-10-21 00:39:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c42edc8-a372-34df-8b61-7cd1492bce89 | -2.8023 | -53.317799 | 2024-10-21 00:39:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c11aa569-1cd1-3e73-a402-7be593a757de | -2.8041 | -53.326 | 2024-10-21 00:39:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc3f211-1151-3c0f-9277-0d0f89f98b0f | -2.8059 | -53.334301 | 2024-10-21 00:39:18 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e127b6-0669-37ee-a5ef-9f710d995a4f | -2.9864 | -54.330101 | 2024-10-21 00:39:19 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5982a4a7-6756-3cf3-bdf6-71786a06bcd0 | -2.9885 | -54.3396 | 2024-10-21 00:39:19 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b93edb7-41e2-31e0-b40d-bcf833f5d25b | -2.9787 | -54.341702 | 2024-10-21 00:39:19 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc5b2171-3205-33de-b0c9-60d2525f3a1e | -2.2242 | -51.243 | 2024-10-21 00:39:20 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39648a7c-2649-3f2a-8ef4-244790d6253f | -2.8048 | -53.975101 | 2024-10-21 00:39:20 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 919aa988-93be-36e8-820d-cb94ee8e1188 | -1.8455 | -50.019699 | 2024-10-21 00:39:21 | METOP-B | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56dbf13b-a200-396b-82a5-2bfd2308a852 | -1.5211 | -48.722698 | 2024-10-21 00:39:22 | METOP-B | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e64ffd84-9552-3672-9cdc-d49636147757 | -2.6818 | -54.761002 | 2024-10-21 00:39:25 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 089a1e98-fc6d-3cfb-81ae-ea8697d1f88b | -2.684 | -54.770901 | 2024-10-21 00:39:25 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be9c7bd6-0bfa-3b75-ad4b-42b274cd9124 | -3.0357 | -50.500099 | 2024-10-21 00:39:40 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c621d1f5-a890-3d2b-b010-1ffc7e4d8400 | -3.1838 | -51.250999 | 2024-10-21 00:39:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd5cd7bf-c3b3-3c8b-82fa-9eda86df70fe | -3.1854 | -51.257999 | 2024-10-21 00:39:40 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d920d48-3b0d-380e-a340-6e0fe16afa0f | -2.7259 | -49.356098 | 2024-10-21 00:39:41 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e454c454-ae93-3696-8a32-58bfd8fef85d | -2.7275 | -49.362999 | 2024-10-21 00:39:41 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c208ed4-fb76-3b09-98c4-91e43310e8b7 | -3.5064 | -53.017502 | 2024-10-21 00:39:41 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e003051c-793b-3a7b-bd1c-65385b941777 | -3.2089 | -51.730598 | 2024-10-21 00:39:41 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30c642fb-7882-3d58-9699-a0382295264c | -3.1654 | -51.582001 | 2024-10-21 00:39:42 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a87ddf1c-b393-3bf1-877d-38a5e2606a0c | -2.9262 | -50.517101 | 2024-10-21 00:39:42 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67de310a-7f75-33e1-8dad-72f65bb0b9d4 | -2.9277 | -50.523998 | 2024-10-21 00:39:42 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e31e0f4-b093-337e-a9d7-b47e27511c7c | -3.167 | -51.5891 | 2024-10-21 00:39:42 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5134c1dc-1c97-39b3-8d72-e87f057c22a7 | -3.1686 | -51.596298 | 2024-10-21 00:39:42 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d597b996-6f78-381f-9726-959da2405d9d | -3.1943 | -51.711201 | 2024-10-21 00:39:42 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daa5b2eb-98fd-3b87-b296-2867135a0b35 | -3.1959 | -51.718399 | 2024-10-21 00:39:42 | METOP-B | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d49ce95-b108-31c3-8615-89fe1ba4be37 | -3.0465 | -51.0979 | 2024-10-21 00:39:42 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2f81ce-cc2e-3a73-b7b8-2754b919c588 | -3.0481 | -51.1049 | 2024-10-21 00:39:42 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93f302fa-2ba4-3417-9460-dd546feda289 | -3.0917 | -51.3451 | 2024-10-21 00:39:42 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b67fd2c1-447b-3f14-b1d1-659084433521 | -2.4296 | -49.094002 | 2024-10-21 00:39:44 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31a2329e-bd5f-3d49-801f-fa5db61b63d6 | -2.4311 | -49.101002 | 2024-10-21 00:39:44 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 871d4ba4-a4dc-3981-aac4-0d13355979c4 | -2.4327 | -49.108002 | 2024-10-21 00:39:44 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 573f2bcf-9a8f-3035-ac5a-90d981e6fe65 | -2.3636 | -48.939201 | 2024-10-21 00:39:45 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5be5e753-082a-369d-9218-0cda34175b6a | -2.2616 | -48.580299 | 2024-10-21 00:39:45 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a981ba7f-be3e-3ba8-b995-4e7df4a65d59 | -2.2632 | -48.587502 | 2024-10-21 00:39:45 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9e929a1-b15e-333d-95d9-98c72004010e | -2.2191 | -48.574699 | 2024-10-21 00:39:46 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 952566b8-b56e-3001-ab3f-4ae953875bd3 | -2.2207 | -48.581902 | 2024-10-21 00:39:46 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a93d6b93-1698-3115-8715-e5498ad6b7af | -2.7717 | -51.3419 | 2024-10-21 00:39:47 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ec6d67e-0564-3510-b521-7eab91e5ea2a | -2.7733 | -51.3489 | 2024-10-21 00:39:47 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4cbf1d30-9f6e-3d11-932c-892fd8d11bae | -2.2548 | -49.096199 | 2024-10-21 00:39:47 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baa5b643-d223-3130-a3f1-1cd3b193a373 | -2.7635 | -51.351101 | 2024-10-21 00:39:47 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dcc50c2-f037-3e7f-abe4-8b775636c9cd | -2.7651 | -51.358101 | 2024-10-21 00:39:47 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20009da0-84ac-3a0a-9cb5-9c5800470fcf | -2.7666 | -51.365101 | 2024-10-21 00:39:47 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 912cb4c5-25ca-3612-9d20-73b6eb5c0f3a | -3.2318 | -53.770199 | 2024-10-21 00:39:48 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0101724c-7faf-3a27-9edd-1a16d1d29f8d | -3.2337 | -53.778999 | 2024-10-21 00:39:48 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9684c7-4a24-3287-ac82-f15ead423783 | -3.0732 | -53.103699 | 2024-10-21 00:39:49 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aead8e47-3714-3a00-b981-41d8ba457079 | -3.075 | -53.111801 | 2024-10-21 00:39:49 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d9bab38-5813-30c1-8378-209f868a3108 | -3.0768 | -53.119999 | 2024-10-21 00:39:49 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c081122-05da-3177-8d3a-1a290503a25e | -3.0786 | -53.128101 | 2024-10-21 00:39:49 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33f463e7-2b8b-3efe-b476-5e4805704af2 | -3.222 | -53.7724 | 2024-10-21 00:39:49 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bc8f458-3525-3b96-989e-4abfe11de26d | -3.2239 | -53.7812 | 2024-10-21 00:39:49 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6fcee12-7836-3029-8ceb-1c377c9200c2 | -3.067 | -53.1222 | 2024-10-21 00:39:49 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50325cc7-d8a4-31f4-85c1-f6317f49a2ed | -2.8852 | -52.445499 | 2024-10-21 00:39:49 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b60659c5-f4d4-3c73-a03a-2c6d90d36286 | -2.8868 | -52.452999 | 2024-10-21 00:39:49 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef0da373-a46f-390c-ae56-bf4928950be6 | -2.9669 | -53.042 | 2024-10-21 00:39:50 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2e2f029-9118-3296-8220-3414400c773e | -2.9553 | -53.036201 | 2024-10-21 00:39:50 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c04da015-b161-3a66-8f95-7945020fa4c3 | -2.9571 | -53.044201 | 2024-10-21 00:39:50 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9645838c-ad7a-3725-9356-8cda3ad9c5f3 | -2.9589 | -53.052299 | 2024-10-21 00:39:50 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfd37824-f6ec-3352-8fe7-49c35df7f69a | -2.9135 | -52.894501 | 2024-10-21 00:39:50 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60513285-215d-3be4-b8fc-fb9fc3466566 | -2.9152 | -52.902401 | 2024-10-21 00:39:50 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae2cf147-2bd4-38b8-817c-04c04b62100b | -2.3547 | -50.450199 | 2024-10-21 00:39:51 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e9cfa27-c671-3480-a7b1-e6ef254154fb | -3.4433 | -55.374901 | 2024-10-21 00:39:51 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56d48f92-f29b-367f-8d58-9a2e61e80477 | -3.4335 | -55.376999 | 2024-10-21 00:39:51 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be686996-11a5-3d73-969b-05898b509e66 | -2.2115 | -51.919998 | 2024-10-21 00:39:58 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2514acf8-fdac-33bf-9589-fbad1e6baa79 | -2.2131 | -51.9272 | 2024-10-21 00:39:58 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7a36af2-464e-3ce7-ade5-bbb6e5deb235 | -2.2148 | -51.934399 | 2024-10-21 00:39:58 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23d9f725-9841-3e24-aaf6-61f3b348a197 | -2.192 | -51.879002 | 2024-10-21 00:39:58 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e82103de-973b-3558-b813-6f40979902b0 | -2.324 | -52.5131 | 2024-10-21 00:39:59 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3f918c6-89a6-3130-a8f1-3367c6ff7330 | -1.6355 | -50.459499 | 2024-10-21 00:40:02 | METOP-B | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43a96e28-605a-32ed-9dec-ea23d2c36aa3 | -1.637 | -50.466301 | 2024-10-21 00:40:02 | METOP-B | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 238559a3-b408-388d-97f4-0f795ae8e432 | -1.9791 | -52.122898 | 2024-10-21 00:40:03 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9024cebf-eb0c-34d2-8141-02387b3015ce | -1.9006 | -52.094601 | 2024-10-21 00:40:04 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1899c33-cb07-3cf6-b194-c39b378303f5 | -1.9023 | -52.101799 | 2024-10-21 00:40:04 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d577dafe-729d-3020-bb13-5897e2d2cd62 | -1.9039 | -52.1091 | 2024-10-21 00:40:04 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9b87307-3518-3480-a1b9-c81c6a3d8bdb | -0.9833 | -48.078098 | 2024-10-21 00:40:04 | METOP-B | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce7334ed-28cf-3540-8f0c-d607c4861688 | -1.8908 | -52.096699 | 2024-10-21 00:40:04 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82a18a55-9053-3064-806d-5d510bdb25a4 | -1.8925 | -52.103901 | 2024-10-21 00:40:04 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d18b227-040b-3d21-97e8-c2d219194efd | -1.8941 | -52.111198 | 2024-10-21 00:40:04 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5465bea-d0d0-3791-a770-86c7f2ab4101 | -2.2891 | -53.920601 | 2024-10-21 00:40:04 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f976466b-f4fb-3541-b49a-7f4187f1e28d | -2.291 | -53.929401 | 2024-10-21 00:40:04 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4331cd33-1676-3b38-b39d-a9c2817b32d0 | -2.233 | -53.715401 | 2024-10-21 00:40:04 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf1756e7-7926-311c-b4ff-d4e74735d973 | -2.2387 | -53.741001 | 2024-10-21 00:40:04 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3865f429-1e5a-348e-9c0a-5958b7ed41d1 | -2.2406 | -53.749599 | 2024-10-21 00:40:04 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2652789f-459a-3d99-8d3d-b49a66eecb77 | -2.2289 | -53.743099 | 2024-10-21 00:40:05 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7e0467f-a974-3f48-9d57-4d79480497d8 | -2.2308 | -53.751701 | 2024-10-21 00:40:05 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 737f16fc-b9f5-321e-aab4-142e75a053b4 | -1.7682 | -52.055401 | 2024-10-21 00:40:06 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1dabce-f35b-3468-9c21-f762e60c0767 | -1.6011 | -52.640499 | 2024-10-21 00:40:11 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bf8ce59-08f8-3420-8881-d23279bb35a2 | -1.1656 | -53.633598 | 2024-10-21 00:40:21 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89483da5-7adc-3b4c-8c16-d97b3af6d3cb | -1.1638 | -53.625401 | 2024-10-21 00:40:21 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b02aa0ea-0642-33b7-a28a-0e8f451e80b4 | -1.1675 | -53.6418 | 2024-10-21 00:40:21 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1495d552-de22-3205-af85-8ef90cf7e139 | -1.154 | -53.627499 | 2024-10-21 00:40:22 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2593f5be-dc89-35b8-b72b-01a185fa5da3 | -1.1558 | -53.6357 | 2024-10-21 00:40:22 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8243fbe-4a9e-3807-bcde-8b150a8fbf67 | -0.1715 | -49.909 | 2024-10-21 00:40:24 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
