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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bc13884-4694-3ac3-a4d6-9562e44e364a | -19.50653 | -42.32536 | 2024-10-03 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 5b519fd5-fc17-3056-8daf-cbb4d8da1d63 | -19.50502 | -42.32 | 2024-10-03 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 0659cf7a-810e-39f0-939c-ba99b83f6430 | -19.50451 | -42.32423 | 2024-10-03 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ad82dada-9416-36db-b638-5dfee70aa1a1 | -19.50354 | -42.33228 | 2024-10-03 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 17e555f0-516c-3704-801d-a830ce091223 | -19.49998 | -42.32388 | 2024-10-03 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c8426fb3-f9eb-3884-aa4d-217fb8701ca6 | -19.49947 | -42.32811 | 2024-10-03 04:29:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1c64235d-72c5-32d9-b56a-3ec9eb5eccdf | -19.314 | -42.60434 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 6e3b7f33-6515-3aa5-934d-921eeb1e69db | -19.3096 | -42.60363 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| bd8ca54d-fac4-3766-a23a-17e4641d24d4 | -19.30912 | -42.60765 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| d0e9ed41-6668-39cc-9491-2eb5ebefc181 | -19.30865 | -42.61156 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 9cc09753-6f9f-3bb2-a224-835230b7a63d | -19.30622 | -42.40114 | 2024-10-03 04:29:00 | NOAA-21 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ce123b4c-03d8-345a-917b-2f7147c64c6e | -19.3052 | -42.60295 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 519a854b-1928-3261-96c2-702a7191125d | -19.30475 | -42.60678 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 31.2 |
| 3d45b91d-89d1-3ead-9fc1-8235f35482c3 | -19.30242 | -42.58859 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 383406af-1126-3977-ae8b-1478b7d6bee8 | -19.30186 | -42.59335 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 000d3747-3118-37ef-bfe0-615ac14a6739 | -19.29808 | -42.58728 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 26b2e690-03d0-319d-943f-4d7e60dd05eb | -19.29749 | -42.5923 | 2024-10-03 04:29:00 | NOAA-21 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| ed50674b-0382-3bbd-921e-3173a8c49aac | -19.27111 | -42.36643 | 2024-10-03 04:29:00 | NOAA-21 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 9319021e-a7e5-3714-86dc-d561e1b76bd9 | -19.26384 | -42.35118 | 2024-10-03 04:29:00 | NOAA-21 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 22e069e9-1498-3779-bf3a-77f981505f85 | -19.25935 | -42.35065 | 2024-10-03 04:29:00 | NOAA-21 | BELO ORIENTE | MINAS GERAIS | Brasil | 3106309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 66ec2914-b2ad-3d64-b629-9e1bcf66d2be | -19.03979 | -43.20067 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| db093701-63d4-3914-b289-0300836176bf | -19.03932 | -43.20449 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 85b15822-ebd6-3be6-b2cf-60cb75afac9f | -19.03884 | -43.20833 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2fa6ae2f-e51c-3f11-9d4c-47316a47fe68 | -19.03553 | -43.20042 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| d9dee91a-2c55-3085-af5a-53645d8a6450 | -19.03506 | -43.20424 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 81daf4d2-bc5b-3e0e-be9d-0089373633d7 | -19.0346 | -43.20797 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2bf8b267-0d98-3409-a0dd-09c686d85c70 | -19.03128 | -43.2001 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 7e41eec0-d76f-359d-893b-f426ca018442 | -19.02517 | -43.21472 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b8853f0-d74c-3d41-bec6-30b8bade2806 | -19.02278 | -43.19933 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| e9b53d68-5687-3569-8b35-cd6d5bb3a302 | -19.02229 | -43.20329 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| d2e390de-541c-39dc-a991-998732ec657d | -19.02094 | -43.21423 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2bdc3af3-2795-3078-ad12-f596b5a99b07 | -19.01856 | -43.19874 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 343865a0-d7d1-3629-9579-d02238713122 | -19.01809 | -43.20261 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 3c769d58-f72a-3054-ba0f-03c3079bb7e1 | -18.98248 | -43.21302 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3f3b290f-c65e-3491-bafe-04887783b6bf | -18.98243 | -43.20996 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2cab34b5-038f-33c3-97bb-d810732169ca | -18.98191 | -43.21402 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 66a6bef3-f9fd-340d-a556-e2f218fc0edf | -18.98101 | -43.22512 | 2024-10-03 04:29:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eca507b5-3fd2-35b2-b264-43655ec386af | -18.98038 | -43.22606 | 2024-10-03 04:29:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0b4c18bc-cbd1-32bc-934b-354d60e3d746 | -18.97825 | -43.21252 | 2024-10-03 04:29:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 65a4a9b6-132a-39dd-b48b-93fa25802b24 | -18.97776 | -43.21658 | 2024-10-03 04:29:00 | NOAA-21 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b5a7d7ae-b0e5-3ea8-aa9c-81df69b2b75b | -18.97769 | -43.21351 | 2024-10-03 04:29:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 065cd88f-5416-3bb4-a73e-69549045c999 | -18.97717 | -43.21753 | 2024-10-03 04:29:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 70c31952-c9e0-3fcc-bf85-9bf23a249f24 | -18.9768 | -43.22457 | 2024-10-03 04:29:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 17ab18d0-4929-3231-a6ba-a0b2d5bb024e | -18.97666 | -43.22154 | 2024-10-03 04:29:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| cbbe4ae2-d5b7-3a51-8e71-063f4cf3aec2 | -18.97616 | -43.22549 | 2024-10-03 04:29:00 | NOAA-21 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 180452ef-b18e-3442-98ec-70d3b0cb918e | -18.33059 | -43.05421 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| cd56e540-f622-3289-abb7-32b9dd0286fb | -18.54352 | -42.24498 | 2024-10-03 04:29:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bf038e6c-1d7e-36d6-b10e-b94f5c920832 | -18.53905 | -42.24438 | 2024-10-03 04:29:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 3b39c6bf-8981-319b-b48f-8838ddfbb816 | -18.53636 | -42.22917 | 2024-10-03 04:29:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d51fcc88-71e8-3e65-975c-50e03e7f77a4 | -18.53465 | -42.24322 | 2024-10-03 04:29:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 2d9771b6-29e9-3cf3-af07-9f83b24db1ed | -18.53412 | -42.24759 | 2024-10-03 04:29:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 3df5ceb8-eff4-36ce-b92c-a690a936a577 | -18.52747 | -42.22753 | 2024-10-03 04:29:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a82a84ff-f624-3fb4-a845-d561f2590f61 | -18.52689 | -42.23232 | 2024-10-03 04:29:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a148b841-3fc7-35a8-81ef-de5311467222 | -18.52132 | -42.24079 | 2024-10-03 04:29:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 0dc228d8-4510-3d2a-9c80-c95abd3b3200 | -18.5163 | -42.24478 | 2024-10-03 04:29:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 93b78bc4-631f-327d-bc2c-1fc9abdef98e | -18.49317 | -42.95667 | 2024-10-03 04:29:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3fbd058c-d78c-3ed7-a595-b6818ee96f53 | -18.29657 | -42.1732 | 2024-10-03 04:29:00 | NOAA-21 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 3c0c26ed-9a50-376f-ac9f-89da7d3be471 | -18.2965 | -42.54062 | 2024-10-03 04:29:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3524786b-f553-384d-b5e1-b8507d5fcc78 | -18.26455 | -43.03239 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 98c988fe-6880-3f86-9666-de25f426bb09 | -18.26403 | -43.03667 | 2024-10-03 04:29:00 | NOAA-21 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 9f90176b-532f-3522-8343-0e1a04086e5e | -18.08603 | -42.6441 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4b715b13-f6f3-3e9c-ae25-e662a3562603 | -18.08373 | -42.64255 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 56e3dfab-2093-3281-80b8-4fbcc73fbaa4 | -18.08318 | -42.64721 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d5be7bf7-634f-3067-9a3b-5b374e6e2fb7 | -18.08168 | -42.64371 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 33807e4c-a7fa-38dd-aa46-238ac2117002 | -18.07144 | -42.62029 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 233792b2-2aef-3304-8743-82a9dfaa7b24 | -18.07091 | -42.62448 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 725332cc-b142-3c63-92e3-aeb2d2b48e6a | -18.06936 | -42.60176 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4800a0b0-8608-37b3-be62-ccf444219ee5 | -18.06879 | -42.60632 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cc9c59db-d478-32e1-be9b-4301287d0bcf | -18.0671 | -42.6198 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 58284049-4fdc-33ec-8c7e-2fb8df0552d2 | -18.0622 | -42.62377 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8df0b150-9ebc-3401-b059-1d1c71552684 | -18.0584 | -42.61892 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ae7a1c8c-858e-37cc-b339-d8d9f3910e5e | -18.05784 | -42.62343 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c0629853-1dd2-317f-a579-263d51a656a2 | -18.05405 | -42.61854 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 8b6c5e7c-a62a-3fb7-9e27-05060bb42f3c | -18.05349 | -42.62306 | 2024-10-03 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| fd677b31-8f2d-327f-8e2b-c01134d6b1cb | -19.42409 | -43.08747 | 2024-10-03 04:29:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2664cc8d-a909-3dc6-9d73-4cd4f5aa3f8f | -19.42359 | -43.0915 | 2024-10-03 04:29:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 02699edc-e5f4-3dec-9ac7-57a4f3d1c12d | -19.42322 | -43.08513 | 2024-10-03 04:29:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 22411fe8-514b-3066-aef9-6841879ff12a | -19.42275 | -43.0891 | 2024-10-03 04:29:00 | NOAA-21 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c8a60fb4-11ae-3810-a635-26d2c1f34d49 | -18.84489 | -42.93129 | 2024-10-03 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 0a2e3030-fca1-387d-a717-f4fe8070010b | -18.84437 | -42.93551 | 2024-10-03 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 42776944-cdd0-3ddd-b02f-7b2b1143862f | -18.84156 | -42.92281 | 2024-10-03 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 19d5640c-549f-39e3-9f56-b71bb226730a | -18.84108 | -42.92672 | 2024-10-03 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fd2a937c-f3d1-3bdc-a0c4-c22b25fbe132 | -18.8401 | -42.93483 | 2024-10-03 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1324a7a0-94b3-3df5-a7fc-fc5908282bc0 | -18.83728 | -42.92221 | 2024-10-03 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a94a447-042c-35d1-b49b-d32880f2ab00 | -18.83679 | -42.92616 | 2024-10-03 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 60a0f5e8-8065-3514-9ed9-56040b05ae6c | -18.83302 | -42.9213 | 2024-10-03 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| ccf4bef2-4d44-3c49-a9b9-7f2bfb44b268 | -18.83253 | -42.92533 | 2024-10-03 04:29:00 | NOAA-21 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 32fc946e-2d71-3530-8849-6733284196c6 | -20.85292 | -42.23367 | 2024-10-03 04:29:00 | NOAA-21 | VIEIRAS | MINAS GERAIS | Brasil | 3171402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 1c2dea68-9c13-395e-8322-54057d60bb46 | -20.80844 | -42.29758 | 2024-10-03 04:29:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| fb4a9bd5-28a2-3e73-9083-7a871d341eb4 | -20.8084 | -42.29832 | 2024-10-03 04:29:00 | NOAA-21 | SÃO FRANCISCO DO GLÓRIA | MINAS GERAIS | Brasil | 3161403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 5624a65b-a4f9-3fd7-8d0c-4cf0794ec8b6 | -20.48627 | -42.47156 | 2024-10-03 04:29:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| cea65162-fea9-32ca-994d-7cdc647d54e7 | -20.21934 | -42.47487 | 2024-10-03 04:29:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| fbe3d7eb-5e64-3561-89d6-0c8d9b98777c | -20.21537 | -42.46971 | 2024-10-03 04:29:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e5a84010-46ae-3c22-8e73-006f276c4cd5 | -20.21482 | -42.47441 | 2024-10-03 04:29:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f783e5ef-78c9-35e0-a7bc-52689c73bff9 | -20.21087 | -42.46907 | 2024-10-03 04:29:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| acb5b106-8f78-3e04-a526-98e30cb108ff | -20.20977 | -42.47845 | 2024-10-03 04:29:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 484c0068-b215-3e43-b79f-13aa17ffd28a | -20.20924 | -42.48298 | 2024-10-03 04:29:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 47c9761b-49ab-354b-a656-75342f6c5aa4 | -20.20871 | -42.48755 | 2024-10-03 04:29:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b1c097fb-bff2-3899-b395-ca802166deda | -20.20476 | -42.48221 | 2024-10-03 04:29:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 99fd016f-e81a-31b8-aeda-0811ff575716 | -20.20422 | -42.48686 | 2024-10-03 04:29:00 | NOAA-21 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |


[Clique aqui para ver as próximas entradas](README101.md)
