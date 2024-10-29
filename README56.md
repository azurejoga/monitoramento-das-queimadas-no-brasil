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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81f9505c-0a06-3bc7-acc9-1f377c815b5c | -7.34351 | -43.57888 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 93784755-a91e-3bcc-83ef-cece34491d0b | -7.33978 | -43.57418 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 0af7dcea-23ab-3c69-8a41-877b60161aba | -7.32462 | -43.58839 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8c9a2cc8-072b-34b9-88ed-2e1635387e66 | -7.32235 | -43.5857 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 01e88123-03a5-3458-9486-25e6b5b6ce9e | -7.32032 | -43.58772 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 88f399df-830f-3424-bdd4-4a359fe9cfbf | -7.30058 | -43.64445 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8351ce9b-ab4f-3954-b085-55880bd23c6b | -7.29999 | -43.64853 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| af11d30f-b429-35f5-9b01-0d5efa097d58 | -7.29513 | -43.65188 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6f931e69-e0d5-3976-b59d-65381ad79999 | -7.29086 | -43.65118 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b7013d71-3517-37d5-9491-bdf38e59948b | -6.83365 | -43.27306 | 2024-10-29 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| e45ba627-daa2-38ea-80ed-2edacc25ca78 | -7.60857 | -43.66486 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 881cc835-4afe-38dc-9960-7d307c06f1f5 | -7.60798 | -43.66888 | 2024-10-29 04:40:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e77734e9-4ba2-357b-8c9e-0a29d00f609a | -7.30631 | -43.26728 | 2024-10-29 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c79e6ef9-71e5-3544-81c0-aac894b7052a | -8.71986 | -44.01928 | 2024-10-29 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d44a349a-9bd7-30f1-ae57-ad6c2d47ec01 | -8.7156 | -44.01866 | 2024-10-29 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77abbdf8-b72b-32a7-8212-a9341da78eef | -9.72303 | -43.91673 | 2024-10-29 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a73e8a46-7653-30e8-86ad-728ec4534b17 | -9.71868 | -43.91615 | 2024-10-29 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 45762d5d-d1aa-3dd6-b190-d91d355a1093 | -9.5288 | -43.02142 | 2024-10-29 04:40:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd7f1700-9f95-33eb-970d-7d237eac0138 | -9.95784 | -43.94799 | 2024-10-29 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2160e3d-b539-3845-98f5-6585edbe3455 | -10.49854 | -44.16439 | 2024-10-29 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67d657eb-65d5-3d54-bda8-dc0922f73b0f | -10.35573 | -44.05296 | 2024-10-29 04:40:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0b7fe25c-e8d3-3584-a82a-032bfafad1fc | -10.2763 | -44.27827 | 2024-10-29 04:40:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a1d9925-ee95-3801-acad-df07e57d3c38 | -10.14438 | -44.02124 | 2024-10-29 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84857b98-8613-3d06-85d5-15fa8c64f385 | -11.90622 | -43.81221 | 2024-10-29 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb621831-faa0-3a57-9fcb-9c4f749e7f1d | -11.9056 | -43.81684 | 2024-10-29 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0611d8db-7e2c-3648-98b0-7e1f2bc448c6 | -11.83618 | -44.70411 | 2024-10-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b62c5c9-2a99-341c-8535-4341f8d418da | -11.10497 | -43.33541 | 2024-10-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 2e8426d5-89c8-38d4-867f-772367831566 | -11.10431 | -43.34032 | 2024-10-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| f2462e82-5496-3f63-bcb0-eff68a329a8a | -11.5422 | -43.98137 | 2024-10-29 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d82b4448-5f38-3bd2-aca0-507cc986e39b | -11.5416 | -43.98583 | 2024-10-29 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed242ec2-0600-3105-8612-91113572ed4e | -11.53775 | -43.98072 | 2024-10-29 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 836e9a14-4f87-3c68-9650-85627b9c4685 | -10.87058 | -44.40918 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b534470-c3a5-34bf-a7bc-0939adcf6b92 | -10.86739 | -44.41057 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bc41714-aa39-3a80-9d78-90b1558a8cb1 | -10.86629 | -44.40861 | 2024-10-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c81f619-df4f-3cfe-82bc-3d44bb0927ba | -12.49868 | -43.79179 | 2024-10-29 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2531616-1724-347c-862f-c3359d57a06c | -12.4935 | -43.79593 | 2024-10-29 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cff201cc-307e-346b-affc-9bfbc396d466 | -12.44103 | -43.73245 | 2024-10-29 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4977913c-7a8e-3c63-a4de-401b3483e67a | -12.4404 | -43.73725 | 2024-10-29 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cf9d918d-674c-3950-ba84-4ce3c1423649 | -12.43581 | -43.73662 | 2024-10-29 04:40:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17f7a7c7-e35c-3c87-9c7d-479d4af59229 | -12.23043 | -44.68581 | 2024-10-29 04:40:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9a296fd6-a398-32aa-aeb7-5fb6f67889b1 | -12.22766 | -44.68343 | 2024-10-29 04:40:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b1b326f-d77d-385f-9b2a-84b4ef1efe8d | -12.22709 | -44.68757 | 2024-10-29 04:40:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 02842769-9d3a-3bb0-b08a-b932a730adb0 | -6.25207 | -43.56805 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d3e8078-baa4-368d-be10-985875c4c2c0 | -6.24786 | -43.56724 | 2024-10-29 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4594498a-671a-3ce0-a742-7e919d44b06f | -6.45798 | -44.67571 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4364558c-a18d-3d3e-b35b-90ef8f522105 | -6.45723 | -44.68081 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4db7285a-dc5e-3174-b103-5b259ffd7594 | -6.45405 | -44.675 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 59bc3ad9-15f1-3414-b6d3-98e6347a4011 | -6.4533 | -44.68015 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 99b946e0-fdd7-3b17-b0d8-3d29ba383220 | -6.45013 | -44.67424 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b94cd9fa-51aa-316a-a71c-66d0fdfd778c | -6.44937 | -44.67943 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 0b0df8c7-a1e1-360e-af87-6a5adcd803f8 | -6.3544 | -44.72459 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa1fbe35-cfd3-3264-8c59-e1b37d9c97ef | -6.194 | -44.5368 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| da097fcb-1934-32d8-949e-7b37364df16d | -6.13066 | -44.30047 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6cb8988-7973-36c5-b918-9b4b77ca8a2e | -6.12952 | -44.29988 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 94d5010f-4582-38a4-9742-272f4152bb3b | -6.12901 | -44.70224 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bbe9de5-6a42-35ed-9709-b89e5ca9f4f4 | -6.07253 | -44.6244 | 2024-10-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 636d5da0-0717-3d24-a1bb-07e1b018e724 | -5.94205 | -43.6786 | 2024-10-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7c4a412f-ab60-3d07-b42f-1fe2857055de | -5.94149 | -43.6825 | 2024-10-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ff5a94d-9b3b-3c0e-a0b0-e62197153037 | -5.93787 | -43.67798 | 2024-10-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fba8e7c5-b5f9-3be3-96c7-765c701f717a | -5.9373 | -43.68186 | 2024-10-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8871b71f-5c3a-3fb5-be5b-af551ed5c626 | -5.93369 | -43.67731 | 2024-10-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3d6acb8b-2065-3eac-9252-c620ebcdb576 | -5.93313 | -43.68119 | 2024-10-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 01e299fa-b37b-34fa-ab95-4fc2927be5f2 | -5.93257 | -43.68504 | 2024-10-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9df8781e-447e-340f-8a90-9afb99164dce | -5.92895 | -43.68052 | 2024-10-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31dc90f3-d6df-38f8-b8a2-ac33b4f19b44 | -5.9284 | -43.68437 | 2024-10-29 04:40:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a39c392-80f6-3a12-91db-c7e2bf82c22d | -5.91421 | -43.95601 | 2024-10-29 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dbbed027-fa90-3609-9b5e-fd59ec86f8fb | -5.91369 | -43.95959 | 2024-10-29 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ec14d5c2-0b1c-38d0-86c8-47e37bfa7be9 | -5.81153 | -43.86051 | 2024-10-29 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 22f81467-9eb5-3795-978d-13c2ddc395e4 | -5.81099 | -43.86424 | 2024-10-29 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0f4a6eaa-47c9-3d5a-a09a-cc36e2166d4d | -5.7233 | -43.78291 | 2024-10-29 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab0d4d10-3c27-357d-b3b5-f29b9dee67bc | -5.72275 | -43.78661 | 2024-10-29 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d081166-8c59-3721-ae6c-4e0f0506f566 | -5.71915 | -43.78231 | 2024-10-29 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f23abf1-547f-30c6-bb89-867d3fbbc0ba | -5.71861 | -43.78602 | 2024-10-29 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45efbabd-e97f-314c-8c93-3390e5f1340e | -5.45015 | -43.5777 | 2024-10-29 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 401a4cf6-7c47-3abd-972f-905d07033287 | -5.44958 | -43.58157 | 2024-10-29 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b53e2bd4-b5f5-3624-8cbf-6a7a39d9ed4a | -5.28902 | -43.40924 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a6d6f01-7574-37ca-8662-9f0ed55439fc | -5.28534 | -43.40805 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 44a0f6b9-2758-3346-8437-75c1601a1c20 | -5.28481 | -43.40856 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 608a9fed-0cd2-32eb-a4b3-526aad6a3ef1 | -5.28478 | -43.41196 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9ad2744a-1e12-3337-8751-16a62541feac | -5.28423 | -43.41246 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c59c1821-e0d7-3ab6-a189-c47ec7e4caed | -5.28061 | -43.40786 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 82d01674-0d3f-3dad-8d06-5c0c517f9f0c | -5.28002 | -43.41174 | 2024-10-29 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f328cb3-3a26-3584-9ede-6a389eabe78c | -5.24258 | -43.74419 | 2024-10-29 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 662d0db1-2574-35c0-a133-88821fb73576 | -5.24201 | -43.74795 | 2024-10-29 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fe2c1075-2012-30fd-a1f9-8892a161ab72 | -5.24141 | -43.74382 | 2024-10-29 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 62bfe6cc-0b15-302c-b16b-cf9e3003283d | -5.24086 | -43.74759 | 2024-10-29 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d7378e3e-1828-38e9-a60e-a47d7817f946 | -5.23846 | -43.74357 | 2024-10-29 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e06b34ea-92d2-3d1b-ab18-74dadd96065b | -5.23728 | -43.74319 | 2024-10-29 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 14475ea4-efe6-313c-862c-0de6397a1a83 | -5.23435 | -43.74292 | 2024-10-29 04:40:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8c5c78f7-12b3-3464-afa3-42484259864e | -5.81299 | -44.13284 | 2024-10-29 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a9b8d0e-c3f3-31d0-b5f5-749b0f0f5c2c | -5.81246 | -44.13639 | 2024-10-29 04:40:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 396f0534-68fd-319b-a023-6a2cfc99911b | -5.67648 | -44.15652 | 2024-10-29 04:40:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 73f7293d-b33c-3e0e-9f1f-380e12179e81 | -5.58132 | -44.31461 | 2024-10-29 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5d81d391-e081-3e40-a0d0-8c7344dc5f81 | -5.33891 | -44.18564 | 2024-10-29 04:40:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b5cc90d9-9d24-37e3-bf56-e2a9175b482a | -5.33839 | -44.18915 | 2024-10-29 04:40:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0b7f9f06-0da8-3064-870e-723adfef7c8e | -5.32278 | -44.75676 | 2024-10-29 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8608f90-7a8e-323f-ac9e-1db88e8d147d | -7.79529 | -45.1301 | 2024-10-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b484151-ebb8-35e8-a837-22dd2fc6642d | -7.61753 | -45.26989 | 2024-10-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e11672c7-a5b6-347f-9d14-eb5473c537cd | -7.61503 | -45.27193 | 2024-10-29 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 02d4db77-9680-3413-9452-31142bd2d177 | -7.17932 | -45.14201 | 2024-10-29 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README57.md)
