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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90517bff-8ee5-3217-b9e5-919938c7136a | -4.67931 | -46.65826 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 72d5912f-ab84-3691-a453-deee3d53a6dc | -4.67841 | -46.66486 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 7e6beb69-230e-39d1-b0f1-d8f345637cc6 | -4.67589 | -46.65213 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 30c8ab85-b3c0-3383-911a-dbef9d1822bb | -4.6749 | -46.65904 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6d631042-bc4a-3a80-bf3b-b469db8e1a33 | -4.67232 | -46.65703 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2cd18a25-f8c5-3100-bced-35a3b6cacc1e | -4.66096 | -46.65637 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 50ac2d5c-8fa7-3dae-a150-7c8338b04d26 | -4.66006 | -46.66267 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 038222bc-e544-3c94-ab2f-339d100ab518 | -4.54789 | -46.6078 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5934f694-751d-3f93-b31d-81c63ee1ac61 | -4.54092 | -46.6064 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7cd2d832-544d-3c54-98ab-9806341ee060 | -3.45993 | -47.66774 | 2024-10-28 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d2a6026-d365-3fc9-8d55-6ed7e30dc6af | -3.10876 | -48.60485 | 2024-10-28 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49834f16-fe85-3a5d-82b4-cd5cae8a5b14 | -3.10266 | -48.60389 | 2024-10-28 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f1a24e9-f982-383c-b84e-a884b542fc6a | -4.92108 | -49.01612 | 2024-10-28 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8751ea53-1dcb-306a-9f5b-0bc5bc64c244 | -4.92044 | -49.02069 | 2024-10-28 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77d80859-cc35-35c3-96f9-2ebc3999ab26 | -4.91958 | -48.63288 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cefbe84d-752f-38b9-96ad-5610d2f7288d | -4.91331 | -48.63205 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69eda559-3eb6-39e2-9df1-33fe96970b2a | -4.9126 | -48.637 | 2024-10-28 05:23:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ad13564-80cd-317c-8662-01bc1d8867bb | -4.48548 | -48.11597 | 2024-10-28 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 27c5a9f5-3e1f-37b9-8232-93cf8e90ef09 | -4.48515 | -48.1154 | 2024-10-28 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12f95099-df3d-3ee3-a086-8a0bf65d0b0e | -4.48476 | -48.12115 | 2024-10-28 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d47a6e11-d195-3917-b4db-d640535a016a | -4.48439 | -48.12056 | 2024-10-28 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c604e920-202d-3861-b71d-a6c77f220c4b | -4.33937 | -48.6348 | 2024-10-28 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5bfac4a3-18f3-39e4-ab82-f3ec21c80336 | -4.3387 | -48.63949 | 2024-10-28 05:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89e205b1-db1e-3564-b9e2-9bf453183db9 | -4.14822 | -48.75269 | 2024-10-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9e7b9e5b-2c41-3191-818a-fee5c7d13f8a | -4.14752 | -48.75747 | 2024-10-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bd94539-9faa-39de-8b2e-5410af1fcaa8 | -4.14684 | -48.76214 | 2024-10-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 47d33857-e5c4-3d09-830a-b09a7e268c69 | -4.14138 | -48.75657 | 2024-10-28 05:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22c3f788-e20a-3b4b-82d5-782d5c5eba3d | -4.0271 | -48.3061 | 2024-10-28 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7f0542e-4648-33ba-a4e8-f0ce4de07b91 | -3.93393 | -48.34684 | 2024-10-28 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f289bb6f-bf2f-3cf7-b418-f6e9d629a00e | -3.93181 | -48.34274 | 2024-10-28 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a953c5d-1a07-351a-82f1-f5c598d2fad7 | -3.93111 | -48.34766 | 2024-10-28 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d765896-b5ce-3a92-adb3-0c4712636164 | -3.92763 | -48.34606 | 2024-10-28 05:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18cf40a8-1d5d-349a-a573-b7a9b38555b7 | -5.41974 | -49.23743 | 2024-10-28 05:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47f90fbd-1e89-3b1d-8fc1-8e9725da4b3e | -5.22772 | -47.94891 | 2024-10-28 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6bad41e0-ef78-3210-b5ce-ec2cfa42c835 | -5.227 | -47.95427 | 2024-10-28 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4396709c-419c-35b8-9a48-243211946bd9 | -8.1387 | -49.48003 | 2024-10-28 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d187d93-5483-3735-999c-d3b069ad33b6 | -8.13806 | -49.48497 | 2024-10-28 05:23:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45101966-dd32-3d84-83b7-215c98783209 | -3.04968 | -50.41939 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3428bd5a-bf85-389d-9f15-71e2cc51f31c | -3.04917 | -50.42276 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4f35825b-7e00-389f-9302-b3de88bd2f77 | -3.04474 | -50.4154 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a219f202-3918-3883-9d28-c49cf33785fc | -3.04423 | -50.41876 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 021b1939-5024-32c5-ad95-5b2c7f99a35e | -3.04373 | -50.42212 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2108906e-725a-3909-83e4-b74e1c6a5312 | -3.04324 | -50.42536 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 876682af-f975-3b54-8ad6-f0b7981bf989 | -3.04275 | -50.42866 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ad9368e-5e3e-345e-a797-0e473a105d75 | -3.03882 | -50.41794 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f271fb80-038d-3300-8134-d92246e5bd64 | -3.03831 | -50.42129 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fb791ce3-5ae6-3845-966f-6f2d2ed933f4 | -3.03782 | -50.42456 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9131ce6d-2f7b-3a58-95fd-938f08c996a5 | -3.03491 | -50.40701 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c99e77b-428e-38d4-83e3-cdbb54615eba | -3.0344 | -50.41039 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fee1bd5d-0ab8-3958-a7a3-e4ac674fbea3 | -3.03389 | -50.4138 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a97fbec-a5c8-335f-8661-5272b1c427ed | -3.03338 | -50.41722 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5023a2e2-df8c-3c4f-b5c0-1e61499de5d9 | -3.03287 | -50.42065 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6aef66fc-96e3-3722-bdf8-ab40aa37ce9f | -3.03239 | -50.42388 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a1893f71-bc50-3453-884e-18390bf3b042 | -3.0319 | -50.42715 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3f4654c-4954-3019-a99b-69cc672f45e7 | -3.02948 | -50.4062 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7f29e48e-06a6-34c3-b587-a7b80c8322a2 | -3.02898 | -50.4096 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1b1d1a94-d4ff-31cd-b353-7d00ab7108ef | -3.02847 | -50.41301 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a75809c0-34c6-32b8-b1e1-781b07189be9 | -3.02795 | -50.41648 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 00b17eb0-af9a-3dac-9678-25bd6f2d5e58 | -3.02744 | -50.41993 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c69c74d-b407-37b3-8860-0fde621a82ac | -3.02694 | -50.42324 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c431f58c-89c8-3267-86cb-f6a90c98f541 | -3.02355 | -50.40884 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1db0b68c-d627-39d4-8d00-b3650676c2fa | -3.02304 | -50.41226 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b9dbb6e5-47b9-3400-aa9d-8a5d5b4114a9 | -3.02253 | -50.41569 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a578ab21-1fe8-3413-890b-59ac418cc7ff | -3.01775 | -50.48491 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4469d625-f3c8-38f3-ace6-2967fc7e90d2 | -3.01236 | -50.48408 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acc357c9-5870-3df4-831f-c2753b1a95c1 | -3.01135 | -50.49087 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53b5e88a-c695-3785-8c8e-8ada5d663725 | -3.01085 | -50.49423 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9abd95d1-0292-3bd7-a5d6-49ca3aa66916 | -3.00697 | -50.48326 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d71b7a7-66ec-3f8c-9f73-ea907d790837 | -3.00646 | -50.48669 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc42fb0f-1ff0-3508-8b90-450b2bc5784c | -3.00596 | -50.49008 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb94152d-1662-3547-9960-c698e268a9a0 | -3.00546 | -50.49344 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a263492b-8e13-3551-bd66-f9d24f31389a | -3.00107 | -50.48587 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3cd1c87-8b34-3c49-b625-9617cf4e232f | -2.98059 | -50.47516 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f2d05eba-e661-3087-adba-ad85082e2337 | -2.9801 | -50.47852 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6cda310e-3958-39d0-a526-6628677ffb19 | -2.97958 | -50.48202 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 017e9b86-5985-30fa-8714-4fab39478380 | -2.97814 | -50.47521 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 08fd6e1b-35b6-3c2e-90b6-139ebddbeb9a | -2.97763 | -50.47851 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 47323153-1881-3e20-8fb3-9ef0e1f9b59e | -2.97708 | -50.48207 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a8937b82-aef1-305a-99cb-daed6bc07c2e | -2.97517 | -50.47449 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1c876603-1fe1-3799-b978-60c03985552a | -2.9747 | -50.47775 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8fd4f2ad-0aee-39e9-a307-759085634c5f | -2.97419 | -50.48118 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d2498cb8-3665-3c14-ac1f-cc6f9bdd1226 | -2.97221 | -50.47789 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dfa1a09e-b650-3857-bf13-100942034f32 | -2.96375 | -50.42485 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 57481a3c-acc0-3665-873d-13f936a062a7 | -2.95834 | -50.42402 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85523f1c-d304-3582-be49-a3f3a07d0076 | -2.95782 | -50.42745 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04f0ffc5-96e3-33c4-a747-58af0f2b1045 | -2.93129 | -50.2709 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da85a96f-3c26-34de-a856-f4b2118e5bf8 | -2.93078 | -50.27433 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dedbabc-72a3-3124-b9e7-a425c4e9b5f2 | -2.9248 | -50.277 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fd4e0e9-28ee-3e7d-9bbf-c2f92b634428 | -2.91933 | -50.27622 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e825ce6-7dfe-3a17-8ff7-d36104f7c586 | -2.91882 | -50.2797 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3d672e6-5ba1-30a3-acf8-bf34806db9f8 | -2.91832 | -50.28308 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12647a6b-bfb4-317f-8fb4-3e685734fdf0 | -2.91781 | -50.28651 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 842e4d91-503e-3210-bcf0-2184af956812 | -2.91336 | -50.27888 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea0f6189-a032-34df-8892-607becc4b390 | -2.91285 | -50.28236 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9647ca0c-1708-3fce-b2b2-dc969404cb79 | -2.91233 | -50.28584 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f503e315-027a-33a2-b8b4-e45c5a736777 | -2.91183 | -50.28923 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 81efc245-5802-3328-8434-adc09eeff1f3 | -2.90687 | -50.28505 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50722065-9ae3-3243-a55e-764cb6258820 | -2.85747 | -50.47131 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b9d7eef-8914-352d-8acf-0525b61f6977 | -2.85699 | -50.47458 | 2024-10-28 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 631e9f74-e828-3d53-88e3-12eab8d3ba1f | -3.6041 | -49.36074 | 2024-10-28 05:23:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README79.md)
