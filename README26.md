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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0135cf47-9328-35c9-8153-c6b2505e7d4f | -15.55261 | -48.3153 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e814e7bc-f63b-30db-979d-9a3946e40972 | -11.12032 | -44.64624 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 32c9e017-a682-3f5f-b04a-89aa304782f6 | -15.09598 | -48.12575 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5e80f07-be66-3cbd-895a-88f4a9bb7d01 | -12.48877 | -47.48457 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8890245f-d3cb-3deb-91b3-e48a225568ec | -13.90569 | -48.12148 | 2025-09-03 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e92f2f6d-ea65-3fd9-90d0-3f69cdb20f0d | -17.1935 | -46.0572 | 2025-09-03 03:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f78aae2c-6a60-3896-afcf-81abc0cd4aad | -17.1925 | -46.06173 | 2025-09-03 03:34:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2246ea4b-12de-3fe5-b65f-7c805c10d0c0 | -10.13991 | -46.2969 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3111623-f085-3800-9a5e-959df92171c4 | -12.67804 | -44.74851 | 2025-09-03 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20dbe4c7-403f-3ebc-8613-5641632c7743 | -11.11946 | -44.64278 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 27a64d3d-7110-3568-a6d5-cada6dd4696f | -15.71834 | -47.67329 | 2025-09-03 03:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 20e5144a-a20c-39e6-b115-d7aeae560c39 | -15.55711 | -48.37423 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ced297a8-6dad-3d2c-9520-3135be248454 | -11.3937 | -43.63192 | 2025-09-03 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b202e2b1-7f4d-35ef-b474-2c898ab470f7 | -15.12171 | -48.16093 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee687966-b7da-3b1c-a4b7-932d6df1aee3 | -12.96284 | -48.0754 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a88adc5b-ae49-3793-9e8c-7da8bfcc95bd | -11.11509 | -44.64014 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb209660-b0ca-3db0-9359-b17beecfb77e | -15.90046 | -48.16717 | 2025-09-03 03:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 77c2f47e-45d8-3fe2-b9bc-5d2025820eb8 | -16.29572 | -45.68951 | 2025-09-03 03:34:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0dc9657-45f1-3d10-8577-d75c2471b1da | -11.11743 | -44.6528 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e3a081ae-951e-3445-b64f-8bf3f32da62d | -14.58044 | -48.05256 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 27d1ba45-6ca5-3d8d-b79c-b0fd8b6e134a | -15.12018 | -48.16766 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 726c1711-9d91-3421-bbba-b01edad075ec | -15.57868 | -48.31318 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4184862b-1dd5-3653-a983-f0f60d202e03 | -15.55946 | -48.41643 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0df39952-3b00-39e6-97cf-82aca0d90701 | -15.55129 | -48.35386 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7dda4a16-bf7d-3005-9f74-34fa542d55b4 | -14.80353 | -48.21075 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 251cdf56-c0af-3fc6-9931-6b0714f25d04 | -15.55543 | -48.41354 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0065f197-44db-3144-912e-692fe36e81ea | -13.32856 | -46.82887 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46d6e339-751c-3fbd-be8c-fbcef02cf0fc | -13.35708 | -46.33522 | 2025-09-03 03:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8631bc84-ace7-301f-975e-0db13dee635d | -15.71876 | -47.67291 | 2025-09-03 03:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 487b15d5-ff78-3642-aff1-20dee34fdcb6 | -13.32961 | -46.82851 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d79f64aa-3386-3f5c-bcd9-94aca7bb5e38 | -13.49993 | -47.03029 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 89d9077c-992f-31bc-a223-8791d289e361 | -11.12167 | -44.66367 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| db5b5c90-a82f-3448-8d0b-a8bf853a96a6 | -13.4807 | -46.82272 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae32a3ba-3b97-3955-ab8c-2d578ede20f2 | -15.56429 | -48.40743 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fcbb887e-3ce8-3c51-9829-2d97e5be6ae3 | -12.49027 | -47.47759 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88a59e2f-79bb-3045-8ff6-5bef38f25a3a | -15.10289 | -48.12784 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b0c9bad6-3f8b-36a2-943b-5c8d0921520e | -11.12266 | -44.66723 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8cbabf35-13fa-3fcb-bb97-8d9da7777ee2 | -14.58912 | -48.04698 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 48611202-b65c-3636-9018-f69576eec3cd | -13.49431 | -46.9235 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39e7cc05-a61f-31b2-a9be-003af72dc133 | -14.56391 | -48.06006 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8eca8557-2300-366f-874d-7206735b3df6 | -14.78401 | -48.16542 | 2025-09-03 03:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9e584242-7ff8-3bc4-bf2b-78fcd814c560 | -10.12811 | -46.25306 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f78afb9-0e8a-342d-a897-614ef28d67b9 | -11.90054 | -46.669 | 2025-09-03 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d042be2-f362-3168-9b4a-9be102ed65ff | -12.84236 | -48.06636 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc251006-051e-3ea7-935b-a102964eb2e7 | -10.73711 | -44.81145 | 2025-09-03 03:34:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a2462d1-bc07-30ff-8858-749a61860384 | -12.84033 | -48.04181 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99b18517-9f82-3eb4-97d7-42f3cda24e78 | -15.55206 | -48.38332 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ff7dcc3d-fc4c-3b6b-82ee-c16bfe0c12eb | -11.11934 | -44.65129 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 263896d2-467e-3758-857b-05cba4961650 | -13.35802 | -46.34061 | 2025-09-03 03:34:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5b866f3e-a9c9-38fa-9e6d-5a4e49f1d260 | -13.501 | -47.0252 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e5a631a0-5ab7-32bf-bb6b-61ff11d92c38 | -10.99127 | -46.83871 | 2025-09-03 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68ab2a1b-b265-3f5b-ab02-58e5bc1a9a9d | -12.84381 | -48.02573 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bd61a3ca-37c7-34bb-8353-641253d1f167 | -11.11838 | -44.65622 | 2025-09-03 03:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb8dbf83-87f4-398a-9188-2754803134f0 | -12.95533 | -48.07219 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c4c572b-3cc3-3c9c-a8d4-1ec0351aa32e | -15.55525 | -48.38223 | 2025-09-03 03:34:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 00b79bba-c051-30cb-928b-3049bb8c23ca | -10.98825 | -46.83652 | 2025-09-03 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0b7a1005-7ee2-3232-895d-fb810fabb9f1 | -13.5072 | -46.93256 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 99dc73fd-d6a9-3326-9edf-21b522f67df4 | -11.3825 | -43.56625 | 2025-09-03 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3acbf74-0e13-31f5-9b94-4a72236a3d1d | -12.83671 | -48.0575 | 2025-09-03 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d47eb53-cccc-3b13-82fd-652adbe459ce | -13.50947 | -47.01929 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1449b3f-0a84-36f1-9373-db1525682cc1 | -13.48786 | -46.92058 | 2025-09-03 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84a987a8-51b2-38e8-ac84-8030271d70ba | -10.1327 | -46.30199 | 2025-09-03 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef635e33-dde6-3298-a0f7-76b6682278ac | -15.10839 | -48.12203 | 2025-09-03 03:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61cf8fbe-ffc1-358c-94a7-b4d7f51c2203 | -11.38044 | -43.60758 | 2025-09-03 03:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0450ac68-bbe2-39d5-98db-c8735c6d86e8 | -22.17279 | -48.83534 | 2025-09-03 03:36:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 7a2c97cb-fbe7-3bf9-8aa1-f7e80d20b574 | -22.17888 | -48.83659 | 2025-09-03 03:36:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| f035938c-ee9f-306e-973b-61f1feb4fcf5 | -22.17395 | -48.82902 | 2025-09-03 03:36:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 5a054130-a3d2-3615-81d0-cb072b5e5691 | -22.86614 | -47.39265 | 2025-09-03 03:36:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5a9df3fd-d774-364a-9c5b-2493904f064e | -20.89454 | -50.10501 | 2025-09-03 03:36:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4068ec8a-3ce1-3c07-80a8-47a3131befbc | -22.70827 | -47.03307 | 2025-09-03 03:36:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 62f6c269-9026-3258-b2a8-ad0500eb8bae | -22.70728 | -47.03728 | 2025-09-03 03:36:00 | NPP-375D | JAGUARIÚNA | SÃO PAULO | Brasil | 3524709 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca333bfc-b1b9-3207-bc2d-013e17e7159b | -21.34237 | -45.48755 | 2025-09-03 03:36:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 233919cb-67ca-3abf-bc71-fdeb6ec72d5d | -22.86724 | -47.38799 | 2025-09-03 03:36:00 | NPP-375D | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0ae93f99-3ecf-3141-b62a-cf4ec6888cc5 | -23.35879 | -47.17341 | 2025-09-03 03:36:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 220bd4c0-1bd2-3e7a-9847-0ba03e7078d1 | -22.75626 | -47.27303 | 2025-09-03 03:36:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6f76493d-1390-376b-8605-a2edb6a0271f | -22.17422 | -48.82934 | 2025-09-03 03:36:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| 294e3c4c-ae6f-3390-975e-f17c96a57c48 | -22.3984 | -44.46805 | 2025-09-03 03:36:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e59d334c-fcaf-35e9-b95e-d5dd0b04ca76 | -22.75319 | -47.27819 | 2025-09-03 03:36:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 37f07093-9c75-3e71-8c61-be251b6d4e30 | -22.18173 | -48.82502 | 2025-09-03 03:36:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 8450164b-355e-3dbd-bc0d-4f033d48c426 | -22.00635 | -45.06363 | 2025-09-03 03:36:00 | NPP-375D | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8a314a73-eed3-353d-b9b0-a28d95db9145 | -22.75642 | -47.26458 | 2025-09-03 03:36:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 96a097bb-6b0d-3085-aa9b-d00fef895022 | -23.35773 | -47.17795 | 2025-09-03 03:36:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 47dc1e20-71f7-3c68-92e7-b9d68a4a2f28 | -22.75521 | -47.27761 | 2025-09-03 03:36:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 78f8e2a9-0e6a-3431-a51d-f0514d5bbead | -20.40959 | -45.69624 | 2025-09-03 03:36:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b23c7187-d95e-3bbb-ba71-d592211773a2 | -22.17099 | -48.84105 | 2025-09-03 03:36:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 45a55eaf-aebf-34bb-9048-d60ac345ff68 | -23.71926 | -47.36786 | 2025-09-03 03:36:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| fa60d350-4e0d-32d7-afb5-e443e900e8e0 | -22.7573 | -47.26847 | 2025-09-03 03:36:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dbae82d6-5c6e-3d83-9268-906d9a668b8e | -23.03897 | -45.54042 | 2025-09-03 03:36:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3b605dd7-cca4-3464-b848-4e12463ea646 | -23.39067 | -45.96312 | 2025-09-03 03:36:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| db7a1ce0-8456-3296-ac2f-1c1072f42a0d | -20.88758 | -50.10303 | 2025-09-03 03:36:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4ff45472-4109-3570-b48d-cefc07c8daf0 | -22.17134 | -48.84138 | 2025-09-03 03:36:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.2 |
| 9a3efa5c-8d53-3ba3-9b2c-2523f6eeb252 | -22.17536 | -48.82329 | 2025-09-03 03:36:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 4ffde9f4-288a-3f2c-bcb4-feef88581091 | -22.75535 | -47.26908 | 2025-09-03 03:36:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0499d338-40c3-3bcb-8c80-479ed7e6cd3a | -23.39591 | -45.96471 | 2025-09-03 03:36:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 50633e83-4996-330b-a750-2dcf3a336e41 | -20.74681 | -47.13231 | 2025-09-03 03:36:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4fe32b0-84de-3642-ae48-c87fdf37d0bf | -20.88932 | -50.09616 | 2025-09-03 03:36:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3e10c9f-05e9-3685-9bb1-31e12c9f6244 | -22.17248 | -48.83501 | 2025-09-03 03:36:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.9 |
| 7e66b465-3f60-36a7-819d-2f884e8c86a6 | -20.89246 | -50.0974 | 2025-09-03 03:36:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 242cc9a9-4bf2-358f-b03a-faec65183017 | -20.75267 | -47.13432 | 2025-09-03 03:36:00 | NPP-375D | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aec0a89c-cfb7-3ffa-b56c-e9354b4d38d5 | -20.89077 | -50.10428 | 2025-09-03 03:36:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |


[Clique aqui para ver as próximas entradas](README27.md)
