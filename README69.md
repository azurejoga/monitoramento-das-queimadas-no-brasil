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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5c417319-b7d1-37a5-a297-fba5a25ae0ab | -17.09607 | -57.37579 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 187d1cda-3c52-3286-84cf-7428c656b687 | -17.08941 | -56.83895 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6f761827-da1b-3dee-a584-c885ddc348e1 | -17.08858 | -56.8433 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 844b4a9b-d226-301b-8c12-f0905cce1cce | -17.08507 | -56.83807 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 05f5b503-5ef3-3cf1-a13e-11be76721269 | -17.07991 | -56.84155 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ead09615-23e3-30ba-aec7-1ff85b6c2fcb | -17.05822 | -56.83714 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 94592b26-1c3d-345a-80da-14f3d0208cdb | -17.05388 | -56.83627 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 32891b33-0c5a-387b-8483-5e191d34d217 | -17.04437 | -56.83884 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b28b0b0c-07f3-3e3b-a195-2de5413b1e3f | -17.02512 | -56.84094 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 6f2a236d-8448-3090-8b68-26905a14eb92 | -17.02183 | -56.83878 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e8d2bc5a-508d-3bae-b5c0-d65d0c849b00 | -17.02098 | -56.84313 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| e5f20769-0d65-3017-8052-0990b6951995 | -17.02077 | -56.84006 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 125eeccf-3a49-3665-be17-e5c29a012da5 | -17.01209 | -56.83829 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bfb0aed1-297e-32bd-ba78-90b12b0f2e7f | -17.00774 | -56.83743 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f839195e-8860-3f43-9cb7-8d84f2176477 | -16.99437 | -56.71778 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4435490d-31ca-3a2c-b727-5e54aaa7be16 | -16.99356 | -56.72208 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6bbcacaf-f029-3a11-83a8-8728110c203a | -16.98843 | -56.72552 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 10c3f858-de4c-32b3-a435-54218cc97fea | -16.98761 | -56.72982 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| bab06bfe-ced3-3a92-9318-d800e4aa4e04 | -16.98493 | -56.72034 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| d716da8a-6686-3d83-865c-8adaa863353e | -16.98412 | -56.72464 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 34368513-a530-340a-a9c7-71d8c4393dd6 | -16.97199 | -56.812 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| e4219236-dd3d-3793-9be5-d2cd72417599 | -16.97116 | -56.81636 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 98b486d2-fd7b-3fc1-ae83-d42b93ced4f2 | -16.9658 | -56.79721 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 150d2de4-c1e8-3ec3-861a-00448bc3361b | -16.96497 | -56.80156 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5d34a607-7216-3498-874f-88798c2e9e24 | -16.95962 | -56.78245 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| cb8f6051-1968-343f-a116-046ad35b9a2a | -16.95612 | -56.77725 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 3166aff8-642b-3004-a14d-903eae8f9bb6 | -16.95529 | -56.78158 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 967a2628-8ad4-3f34-a179-1b7483a649dc | -16.9344 | -57.47716 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 23b1a25a-946d-3580-baa3-e978ac3abc12 | -16.9244 | -57.48009 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.2 |
| 2e86d0ec-88e3-36ce-bab2-d62d15ac0a4f | -16.87125 | -56.7437 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 49a62bf2-4337-3f74-aaa0-c2603f991623 | -16.8626 | -56.74195 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 5c30501e-0c20-38ac-99c7-176f82106cd9 | -16.8511 | -56.70821 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 5ae6b595-639e-3bde-aad2-25053f3e8a79 | -16.84944 | -56.71683 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f68d8b9b-ba4a-37ee-ae70-659345d11851 | -16.87133 | -57.6773 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| be28ab7b-df9a-3933-a917-6393c469cfff | -16.87104 | -56.7212 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2ec78a96-483f-3352-ac1f-e7498484e86a | -16.86775 | -56.73849 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1c0d48aa-b8f4-34c6-8d03-4454bd1b93b4 | -16.84795 | -56.748 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 75f9c438-60c4-3e78-a491-07c762c09c1a | -16.84695 | -56.7298 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 9b502243-1adc-30dd-8dae-8bbef0624301 | -16.84678 | -56.70733 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 429c6328-ee16-3c81-970f-9765d43ef3e5 | -16.84262 | -56.72894 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b67942be-567f-3aef-a41d-d785f7b522d6 | -16.84007 | -57.45013 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| cb03a865-1e7d-3818-b386-3a51fa98d711 | -16.83913 | -57.45494 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7b1f3364-004a-3aff-a745-2f478e2b3683 | -16.83554 | -57.4492 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e2c6aa11-49f2-37f0-8a0d-aa2ca408bb0c | -16.83288 | -57.43867 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 34e14c31-d34f-3aea-8b54-17496bcb2417 | -16.83194 | -57.44346 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| a4a923eb-0c00-3c7d-b12f-ff0eb306107e | -16.81706 | -57.49551 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7b58fed3-a96f-3709-9ea0-24ba45abc757 | -16.81306 | -57.41967 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 5e8b1738-5bb1-3fb7-b03a-ef4b7e17b2d3 | -16.81254 | -57.41714 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 90a9c881-7b69-347d-8da8-4664b5aa38c4 | -16.81163 | -57.42194 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6ad164ce-1d1a-36cf-be32-4018fc6d721f | -16.81072 | -57.42674 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e925b2f4-2a6a-3c27-a217-f8e4b6c74a81 | -16.80947 | -57.41396 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 24186249-a314-3b6d-9a83-9854d5f0e282 | -16.80892 | -57.41142 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| c388c452-0f03-3255-b88b-7433fb390f01 | -16.80853 | -57.41874 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 1a2d596b-cc9a-3c39-b753-9df62dcb1e40 | -16.80801 | -57.41621 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 9f99b677-27e7-3b77-b942-9497485f1bf1 | -16.80759 | -57.42352 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 83cb115e-bdbc-35c0-b567-519da07afb21 | -16.80711 | -57.42101 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 80ae5f18-ac05-3433-a705-e815d9c7a0ca | -16.80665 | -57.42831 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 024335cb-94d1-3d7e-9714-7760d950c115 | -16.8062 | -57.4258 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 7ac3a5bf-278a-3838-b934-e9cf4416c943 | -16.80571 | -57.43309 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 99ef341d-ccbc-3f2c-b1fb-118e69c9f2fb | -16.8053 | -57.4057 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9f912e79-6d62-35a4-8ea4-e85f68f5bd38 | -16.80529 | -57.43061 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 7efab5f2-b911-325c-8519-9469c39bfcf3 | -16.80495 | -57.41304 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4cacd0a9-752f-3b28-963c-d9dacd0d9b88 | -16.80477 | -57.43788 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a1e46028-b678-37b3-868f-3d314a3e8bfd | -16.80438 | -57.43539 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8cd6ceef-7974-3e4a-b817-1e286d641258 | -16.80401 | -57.41782 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 0dbd2e65-dd66-32b9-9e2e-5e2488a97c1e | -16.80349 | -57.41528 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 2c898d2d-413f-3570-a627-967302d1aa52 | -16.80306 | -57.4226 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 2d25c9ce-6314-32ea-a7c6-5a8316fbdd85 | -16.80258 | -57.42007 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 9f1dd3a7-2658-30eb-8792-f7d1e796d088 | -16.80212 | -57.42738 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 0f0fd079-262d-3e52-8df0-f3ace99c91e7 | -16.80167 | -57.42487 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| de0cf4fb-7520-3567-94af-35e6de9ef9de | -16.80137 | -57.40734 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1b2f7a34-3bff-3249-8f6c-f598b93e9556 | -16.80118 | -57.43216 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 0ef879b0-473d-3348-9462-ec0d6c7183bb | -16.80078 | -57.40477 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ccccf10a-0f61-374f-8be4-bd939edf7f71 | -16.80076 | -57.42967 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a31bdd01-c756-3958-85e6-a9bcb7f46fdc | -16.80024 | -57.43695 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c0c687a1-4716-364a-b61d-b02a7e7a56b5 | -16.79985 | -57.43446 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1ac34cde-a681-3b81-9bfa-f545cba9d04a | -16.79948 | -57.41689 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 0a181261-82bf-3a20-94b1-b29cf6ade2fa | -16.79854 | -57.42167 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 38b0e8e5-62b6-3158-9e11-11f9c1c41c09 | -16.79805 | -57.41914 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| d4a6f3fc-2a57-344a-b4a9-9587bfd90bf1 | -16.7976 | -57.42645 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 874bad11-b826-3a02-b9c6-83f143a845fb | -16.79714 | -57.42393 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9cad8d40-dcc7-381f-8d48-0f18a6b6a3e5 | -16.79665 | -57.43124 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 370f47d3-365f-36de-81a4-f04dc05388c6 | -16.79623 | -57.42874 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| bcc0d232-86d5-3447-a456-1ad180160293 | -16.79571 | -57.43602 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0024ffda-5c0c-3fc7-9190-d41753419a85 | -16.79532 | -57.43353 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 80f69a02-af3d-3be3-aacd-0b960987ef2d | -16.79441 | -57.43832 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e5f0a354-7b26-30f5-a77a-fc2bcf208e13 | -16.79381 | -57.44563 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 62acc57d-60d7-32d3-8941-b4f104a7ed20 | -16.7935 | -57.44315 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e4a333f3-68fd-3a17-bec3-1719ae1e3bae | -16.79286 | -57.45044 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bf50202a-3708-334e-bf2f-7efe979c8a70 | -16.79262 | -57.423 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7f6a918d-69d2-3513-953c-ceac8af34629 | -16.79258 | -57.44797 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 74933065-76a5-3f20-8a3c-99d170ef8ac1 | -16.79171 | -57.4278 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 6853ef95-7597-3910-b224-712c9d9e3cdc | -16.78626 | -57.43167 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f847d4b1-5102-3f7e-86c7-371ec9ecada3 | -16.77892 | -57.47022 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 5ac009e6-958a-3085-a344-ca5a32137fdd | -16.7753 | -57.46445 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| e51191dc-93fa-3f4d-8bdd-7d590d680ca3 | -16.77437 | -57.46928 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| cff59613-7aaa-3a8e-bf79-6ec122e75b2c | -16.77345 | -57.47411 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6633b89c-14d9-3799-bc76-c6c4e93f4d7e | -16.76789 | -57.5032 | 2024-10-08 04:36:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e7fdbf95-b362-3755-ab9a-c2a60d663871 | -17.16179 | -56.75008 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 9d816cbb-5a9a-38b3-ba84-359bfe431ca3 | -17.16014 | -56.75864 | 2024-10-08 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |


[Clique aqui para ver as próximas entradas](README70.md)
