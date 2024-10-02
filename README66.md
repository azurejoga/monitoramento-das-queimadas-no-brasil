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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a597931-ba00-384d-b3c0-a6fe3cbecc7d | -8.17967 | -43.66124 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd92f90b-c9d4-39e2-9c44-cb7bd2f2db03 | -8.17568 | -43.66047 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2729bd0a-6e9c-3a4b-8a6a-d680147710e4 | -8.1659 | -43.66943 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1df25342-7b17-3b92-8c0c-be791fb79361 | -8.16189 | -43.66869 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35a48bb9-450b-344a-8bcc-517e02268a88 | -9.15271 | -43.16196 | 2024-10-02 03:53:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cfce4411-9442-333f-b24f-5e3792a4ea65 | -8.32078 | -42.82122 | 2024-10-02 03:53:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f5fea9ba-8d27-3709-9ca7-17c46c6c00a1 | -8.14673 | -42.90664 | 2024-10-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 97c8b952-9798-396b-ab21-02ffc2eee780 | -9.05771 | -42.98713 | 2024-10-02 03:53:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 40bcb14f-612c-338f-9101-df38ffb1d95d | -8.31698 | -42.82057 | 2024-10-02 03:53:00 | NOAA-20 | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5e8c460f-dc64-36bb-af5b-b1643c3e3843 | -8.14405 | -42.90849 | 2024-10-02 03:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2b2ce49d-4b89-3dd2-96fb-3eec317330f8 | -8.17731 | -43.67524 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eba98537-7481-3ae8-8c59-dc6fafaff027 | -8.17613 | -43.68223 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7dd2026-aa71-34f7-b9ba-298641468c86 | -8.1721 | -43.68157 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23d58cba-159d-3224-919c-b0bd4a52a709 | -8.1715 | -43.68511 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8df1a151-cb20-3d6a-be7e-2170f3f6a1a2 | -8.16749 | -43.6844 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a681035-ef9a-3d4a-8958-b839da847194 | -8.16286 | -43.68729 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7660cf79-5384-337d-8979-37b7653c2589 | -8.16225 | -43.69088 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d9bbfff4-898f-3e9c-8270-f4a80bfc56ba | -8.15884 | -43.6866 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ef1e32e-af5a-3198-ad0d-bda2f26ad116 | -8.17672 | -43.67871 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97485ca6-28ac-370b-acee-99ee9ebd0db5 | -8.16688 | -43.68799 | 2024-10-02 03:53:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81cdf6f2-2deb-35be-ba83-45fce214f2df | -9.48226 | -44.0607 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dcb6019a-d5b9-3f51-b4ae-2e08f2d1f0fa | -9.46947 | -44.06258 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 051d5dd0-335a-364c-aff3-f0037862222d | -9.47821 | -44.06009 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b0dee4f-e151-38a9-b109-44ca430ae0b7 | -9.48631 | -44.06131 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53a545a7-8f62-3776-91d6-fd29d73c7d29 | -9.47353 | -44.0631 | 2024-10-02 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cece6953-e81d-3a3f-98ae-1f357e843bde | -7.69677 | -44.93021 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d07cee86-42c0-3aa1-aa5f-47ede8eb4b64 | -7.56929 | -45.01313 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 55185af2-d973-3c8a-8c3a-3eaae484b5fe | -7.5011 | -43.92297 | 2024-10-02 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5ab09c7c-c013-348a-9d6c-3604033f5aec | -7.44379 | -44.85264 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 14d5a05f-575e-329a-b422-f01197f1bc15 | -7.69752 | -44.92592 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af122749-217a-308f-a121-d748b22fa209 | -7.5737 | -45.014 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 61c8ca66-4345-33f9-bc89-5a3c3cc84d9c | -7.50049 | -43.92662 | 2024-10-02 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9d3b8cd7-fb89-3437-b4d7-cdf49171ad5a | -7.42838 | -44.83701 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ab4bae9-df6a-3e93-924a-e01a5e1e08d2 | -7.42327 | -44.84045 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 45dbb48c-ab3c-367f-a5fc-2f04392bc0c8 | -7.57081 | -45.01026 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74fb75e1-240a-3847-a96f-aa886e5cd557 | -7.4452 | -44.84435 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 18266d8c-01a4-3739-8b4a-86e84dd16287 | -7.4229 | -45.24743 | 2024-10-02 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50299170-4110-397a-bc7c-951ed065dc86 | -9.01607 | -45.21926 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 678ee9f2-1754-3bf2-8afd-c35f1cac3f25 | -9.01535 | -45.22343 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d4a3d5e-3f7c-3a69-b68f-c56abd55a713 | -8.89511 | -44.09805 | 2024-10-02 03:53:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20639878-505d-3d67-906e-e4435a6779a1 | -8.83852 | -44.25709 | 2024-10-02 03:53:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbe49783-0f3c-3101-9dc7-fdba61c861fc | -8.71159 | -45.22671 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 212a9241-8aff-3647-a0f7-ddf929c8823b | -8.71079 | -45.23116 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42007f1b-9362-3bd8-bddc-e0e0910f4c91 | -8.70164 | -45.23594 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 20ab769c-b2d3-38b1-87d9-e76689603cd4 | -8.70089 | -45.24036 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 65bc151b-9ac6-38cd-838a-3fca417f01b1 | -8.6965 | -45.23937 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a93f506-cb8a-3c18-8f3f-6db9dc0327e3 | -8.63243 | -44.0692 | 2024-10-02 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c28e028-37c0-3840-a79c-54e8c38e4a54 | -8.23187 | -44.35278 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba7326ae-24d9-3da1-b383-c9af04ac593c | -8.21316 | -44.35837 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6a1352b2-5e99-3b24-a1d7-17c189c5796c | -8.20832 | -44.36144 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eac5ef44-ba9a-33cb-b1f2-5a4881c7ec46 | -8.20349 | -44.36446 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 00a12c96-0f2f-3347-884c-53d50164ae66 | -9.00796 | -45.23998 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2526432-eddb-3f42-bf5f-ccaade60f696 | -8.89448 | -44.10176 | 2024-10-02 03:53:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f4b767d5-ca94-3a6b-8289-fd07678d1292 | -8.72607 | -45.1726 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f9f9e42-a475-327a-91e4-340b5fe8a5d9 | -8.72535 | -45.175 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ae17aef-cc43-3414-80ee-c042cec8b53f | -8.70833 | -45.2234 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff68f13f-7087-3e6e-98a3-01e322e05055 | -8.69727 | -45.23492 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b43642bc-8e40-3d82-9366-56cf78967e36 | -8.69288 | -45.234 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70327279-a669-3cdf-ac22-63209ba0954b | -8.52784 | -44.72562 | 2024-10-02 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 33598676-c418-3544-966b-82280655b4b0 | -8.46148 | -45.10814 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33758dd9-0faa-3616-af28-01e0c7e573e2 | -8.32946 | -45.34887 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94acf001-9430-3512-bc40-4457d4afcf0b | -8.2263 | -44.35994 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bb749f4d-526a-3901-b480-e8ca91f6ce22 | -8.20481 | -44.35661 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 02c3f00c-6391-35b0-bfe7-8bcc5e1abedc | -9.01387 | -45.23199 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0b8e595-c6b7-3707-8db5-465b5b6c87d0 | -8.69135 | -45.2429 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac4a0190-d80d-3cc5-8b65-c05929a17ede | -8.63305 | -44.06558 | 2024-10-02 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4d5803e-6620-3e54-8a58-cc5c98d90c68 | -8.33557 | -45.34022 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6d0e92a-db74-3589-b6fc-e91f14a5e174 | -8.33476 | -45.34489 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c40332f-9d54-38d4-ba16-72c9f438759e | -8.20898 | -44.35749 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad898594-8b11-324c-b32a-dff1d961eed7 | -8.20415 | -44.36053 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 224a30c9-97fc-37b2-a179-96fd0bdafaee | -8.20282 | -44.36842 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b2e72c6-db2c-3bcc-88f7-1cfacb16dbee | -7.94244 | -44.81793 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c1612b4-83b2-3ef7-b596-904caa279374 | -9.01461 | -45.22768 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f1d2618-39cc-3ae1-beea-8e34618cacbb | -9.00945 | -45.2314 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4ca4dae-f2fc-3f7c-9efb-6f06b2923a97 | -8.72612 | -45.17067 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95104c9f-2432-321a-ac97-7ba352ea19e8 | -8.71195 | -45.22886 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6022365f-11f8-3305-aa4a-c6cd08ce1b95 | -8.70679 | -45.23243 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66c15006-2bd3-3777-8c77-fb53666fab9a | -8.69212 | -45.23844 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a2af11a-ab1d-37c4-a7cb-80eda26a01da | -8.68848 | -45.23313 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8437c9a-c6c9-3abb-bb12-5c23ffdf8afc | -8.68696 | -45.24197 | 2024-10-02 03:53:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbf8eace-d00b-319c-ac0e-f6bc8aa09599 | -8.20965 | -44.35353 | 2024-10-02 03:53:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 94caa818-6a5c-3991-a690-297f33d933bc | -7.71505 | -46.16472 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbac608a-1069-31a7-84ab-f95a241afd4f | -7.1029 | -46.4515 | 2024-10-02 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa7f68d6-d2c5-330c-b30d-17c89ee92e10 | -7.10171 | -46.44912 | 2024-10-02 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c841a210-95da-39e2-9981-cea180fdce69 | -7.09801 | -46.45044 | 2024-10-02 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a934769-04d6-3201-95b8-4cc3d0174400 | -7.80245 | -45.48094 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4819decb-7bd6-3a93-8010-8ddb47529ef7 | -7.71351 | -45.42584 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5e16b275-b45a-3906-b412-aee82a4886b0 | -7.7979 | -45.48013 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 568f8f5e-c101-385c-a271-1a61ec0c5232 | -7.716 | -46.15931 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bab42db8-0271-3c26-87a8-917276744f6e | -7.60964 | -45.50623 | 2024-10-02 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35280d4d-04f8-3501-bb6c-8f981045a2f3 | -7.59963 | -45.50948 | 2024-10-02 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35545b37-febc-3cf4-8405-a9a82b2f7e68 | -7.79867 | -45.47736 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9113a4c-3b85-318f-b7a8-67798fe2d28a | -7.71272 | -45.43032 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b5cae0bf-705a-37f9-8627-fe8e35d78d72 | -7.71252 | -45.42753 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 86b42d97-af5e-3431-bafb-a2ab148262ee | -7.79777 | -45.48241 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24fd8228-12c0-3d49-82b5-bedd11c69e01 | -7.79334 | -45.47933 | 2024-10-02 03:53:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49acb2a8-c64a-3689-9af3-89ad2794361a | -7.60503 | -45.50561 | 2024-10-02 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10d7a644-abc5-3ba0-b004-32b307980202 | -8.6229 | -46.53999 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bd12389-fe43-3022-b609-13d4e185d204 | -8.61419 | -46.53307 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d458db9-68cf-32ed-b5f0-28470d968d7a | -8.60845 | -46.53725 | 2024-10-02 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README67.md)
