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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 071c9005-1fef-36ee-af8d-c355e6eddd0b | -15.19858 | -47.96084 | 2024-09-27 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0891f659-d381-3709-bbd6-3b610080c71a | -15.55213 | -48.46836 | 2024-09-27 04:42:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41ce5332-0743-3403-a68c-2c9a29f3a0a1 | -17.77032 | -48.7688 | 2024-09-27 04:42:00 | NOAA-21 | RIO QUENTE | GOIÁS | Brasil | 5218789 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9262d853-ecf6-3ab9-a0a1-5085a520d69b | -17.70625 | -48.47755 | 2024-09-27 04:42:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 823d2e1f-27b4-38d3-8d5b-71698bbbf351 | -18.10623 | -47.98372 | 2024-09-27 04:42:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f51e2c3-c7e4-35de-be2c-81733366623f | -17.50187 | -47.82795 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 46a23420-e07d-3b38-bf46-a4971c4c5c71 | -17.50122 | -47.83269 | 2024-09-27 04:42:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b83e4d77-d758-33a7-81d3-9ec2f6e6189b | -17.22379 | -48.02662 | 2024-09-27 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 184fb519-68c2-3244-95b4-6581d15c5bb6 | -17.15262 | -47.64144 | 2024-09-27 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b8590c5e-ae84-3bec-b718-81b4a2ee06b2 | -17.15198 | -47.64624 | 2024-09-27 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 84b24489-c7be-3d1a-b3cb-747bafd84bab | -17.15132 | -47.65112 | 2024-09-27 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9756a7d6-e9a4-3a2d-ab9f-27e2e69680bc | -16.85128 | -47.70004 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44a74097-4288-3c2a-aa68-d1cb8f3f1477 | -16.85046 | -47.7618 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a04250c-5d89-3c9b-8488-a6f00cbb4d42 | -16.84982 | -47.7664 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 766a0b63-a82e-3ab7-bfa6-5217dd4a32f4 | -16.84918 | -47.77102 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b93eee4a-613d-35e0-b38d-0df4ba9fd53e | -16.84752 | -47.69942 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc83c9d5-188d-34d9-aa3c-b85d55ef5aee | -16.84687 | -47.70413 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2183a29-b002-32db-8444-edc6db9cfd29 | -16.84606 | -47.76589 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b5e3d676-b050-368f-aa97-fa630728b0a5 | -16.84311 | -47.7035 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f154542e-4c9b-3661-9696-467a0328e21b | -16.84291 | -47.76087 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8138fa77-fee5-3694-8043-185b309b77a7 | -16.84247 | -47.70819 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0c1b5273-2287-3377-a0cd-d6ac0470353a | -16.84229 | -47.76539 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 59f194c8-6efd-3211-974a-c075dfb3c497 | -16.83871 | -47.70757 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| afa438ba-b3b9-3276-8e85-a6683c4da07f | -16.83852 | -47.76489 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0246ba0a-a715-3dcb-bf69-d97d72986bab | -16.83805 | -47.71231 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6d50ff94-4f34-3f6e-8a90-7d665b0da997 | -16.8374 | -47.71711 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ae0200cc-13c1-31ed-aab7-325f4a87c6e5 | -16.83416 | -47.7408 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 86d4372b-6bf3-37b8-a758-149877657c5d | -16.83039 | -47.74025 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 18af2fd2-916e-3155-b919-31b46c60bbaf | -16.6831 | -47.83033 | 2024-09-27 04:42:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa64159c-ffa5-36a8-9c95-cac000eaab49 | -19.32117 | -48.91868 | 2024-09-27 04:42:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e6f79bb-756f-305c-b5a5-6cdd7892120b | -18.71799 | -48.14201 | 2024-09-27 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9a598635-d9b3-3074-8199-081602ee555c | -18.71422 | -48.14149 | 2024-09-27 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 77e497e6-bea1-3a9f-be91-902ca253a551 | -18.59141 | -48.98721 | 2024-09-27 04:42:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0d5d162-f711-3d7b-9873-dfa9b76bfc44 | -18.58842 | -48.98224 | 2024-09-27 04:42:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 587b46b1-7115-3cde-800c-fba525620031 | -18.58782 | -48.98662 | 2024-09-27 04:42:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0a02e5a-73e2-3eb8-8dfd-64e4db4140a5 | -18.13057 | -49.08117 | 2024-09-27 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9370dcd9-abbf-3694-9574-500416534bce | -18.12997 | -49.08549 | 2024-09-27 04:42:00 | NOAA-21 | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df2c76cf-3729-3bcf-aca3-3cb5163a5d76 | -18.9411 | -49.17649 | 2024-09-27 04:42:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e319fc2c-141d-3e7e-8cfe-0a1a19173c60 | -18.90051 | -49.15271 | 2024-09-27 04:42:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d2a90473-358e-3af7-90dc-962a5f17a845 | -18.59804 | -48.80499 | 2024-09-27 04:42:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8ce8c7c0-7120-3894-8148-dc3da7f957dc | -18.59743 | -48.80943 | 2024-09-27 04:42:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.8 |
| d72edf3e-5f27-3ffb-81ad-cf7868458671 | -18.26419 | -49.15956 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 2db2f5ff-dbd2-3336-9b68-a17b01802129 | -18.26063 | -49.15904 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ba1020cd-7196-3843-b890-503aa2909a49 | -18.19236 | -49.10779 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9ad9dc11-a9c5-3f03-85b1-7cc031e9c33b | -18.19178 | -49.11185 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9fcf8794-597c-3783-8204-e22caa635ac6 | -18.18879 | -49.10732 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1c29ed49-65fa-32b7-8bbf-7fb43590d478 | -18.1882 | -49.1114 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 40aa0537-165d-34a0-9210-5c4b110b8526 | -15.05729 | -48.61675 | 2024-09-27 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49e0e1b2-38a3-374a-ab6c-a13395972e16 | -15.14023 | -48.77014 | 2024-09-27 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 219a310b-b64c-3626-9d4c-ced39ac0f781 | -15.13672 | -48.76961 | 2024-09-27 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fb37c314-ccfc-3d0f-b769-7b0cb0496cf2 | -15.07752 | -48.94531 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78bdcd92-ffce-365a-a4a3-71d3b6ff9ef1 | -15.06082 | -48.61733 | 2024-09-27 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 87f25420-f173-3741-ac6e-63b2e6a84232 | -15.05788 | -48.61269 | 2024-09-27 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a40da76a-823e-3233-8242-231689bffb84 | -14.86951 | -48.90786 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2eec8cb6-4866-3b9d-a8e9-ef9587c1a0ae | -14.86082 | -48.91856 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24bc8aaf-2378-3110-996d-d03ff2e225a9 | -14.85677 | -48.92191 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9095a9f9-aff1-3ba9-851c-bf2cb5dc9fdb | -14.84984 | -48.92074 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba08ddd7-b80f-34d2-b3c3-1c4f5cccc9ac | -14.84638 | -48.92009 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 530f2a5e-af03-3906-8916-34e37bfe03cd | -14.84291 | -48.91951 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f502c9cf-fcfa-320d-acb4-93e5b7a38f72 | -14.77923 | -48.89298 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 43ce3e16-b439-3e4e-9e7b-ebedeffed8e3 | -14.7769 | -48.88449 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bd6240a3-7306-3f02-842c-f6fbb8c26902 | -14.77633 | -48.88848 | 2024-09-27 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8587f4f9-9590-3b61-982e-a58795e66598 | -13.81044 | -49.62221 | 2024-09-27 04:42:00 | NOAA-21 | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31edd1dc-7e1d-34fe-853b-a41eb68e1532 | -16.68819 | -49.14226 | 2024-09-27 04:42:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64d3bd21-452a-343b-b265-18f472debfa8 | -16.68762 | -49.14634 | 2024-09-27 04:42:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7f34592-3883-3cd7-8ac0-bdfe6a7dd043 | -16.45835 | -49.02748 | 2024-09-27 04:42:00 | NOAA-21 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12786a3a-7aa5-3ebf-b215-fa39acd47613 | -16.31462 | -49.26892 | 2024-09-27 04:42:00 | NOAA-21 | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f96ca13-e668-3088-ad06-7daab69e1010 | -16.31404 | -49.27291 | 2024-09-27 04:42:00 | NOAA-21 | OURO VERDE DE GOIÁS | GOIÁS | Brasil | 5215405 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fec95fdd-f28f-3319-a1d8-19d25065e552 | -15.84859 | -49.12257 | 2024-09-27 04:42:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac5955f5-1543-3975-ba40-18da7055287f | -15.77729 | -50.13675 | 2024-09-27 04:42:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b6ddff8-2e87-330c-9aca-4e8f73ac0060 | -15.47405 | -48.88469 | 2024-09-27 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| aba71d97-fccc-3d87-b74c-d18c214fd308 | -15.47347 | -48.88869 | 2024-09-27 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f6a1dfe2-501b-3b68-8620-f0ad103a195d | -15.47113 | -48.88012 | 2024-09-27 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4bb1eaf1-06dc-3879-a6e4-d63c73968ced | -15.47055 | -48.88412 | 2024-09-27 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| facd6399-29c6-34f0-9772-c410912c9d4d | -15.46997 | -48.88814 | 2024-09-27 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d7ae70a5-7669-36d4-ae56-6e87b3bdbf20 | -15.46705 | -48.88359 | 2024-09-27 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bbe9cba9-c26a-387f-8192-91a5df6142b6 | -15.43343 | -49.01746 | 2024-09-27 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51f7129e-f82f-3c57-b44e-eb19bb9ad487 | -17.25816 | -49.97309 | 2024-09-27 04:42:00 | NOAA-21 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48008c03-c989-35a2-a0db-f71d5689b855 | -17.25474 | -49.97256 | 2024-09-27 04:42:00 | NOAA-21 | EDÉIA | GOIÁS | Brasil | 5207402 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 826834cd-f0f0-35b8-9590-1f285bd6830d | -16.69171 | -49.14275 | 2024-09-27 04:42:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 089f5451-fd70-3259-b9c9-0fb11796ff4f | -16.69112 | -49.14684 | 2024-09-27 04:42:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 694f6ea3-778b-36c4-942b-dbe1b7d6e881 | -19.29829 | -49.68742 | 2024-09-27 04:42:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3fa41ed-fce2-3269-9556-bd0d748c7144 | -19.29654 | -49.67456 | 2024-09-27 04:42:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63ca8aff-6bab-3fcf-ae53-32eef7b53f26 | -19.29595 | -49.67863 | 2024-09-27 04:42:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae36d00c-b03e-3a40-b5ce-aaed34db3cea | -19.29301 | -49.67405 | 2024-09-27 04:42:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 594e8d98-fecd-3c1e-8118-18149e7d40fb | -19.29243 | -49.67814 | 2024-09-27 04:42:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e00f9b65-2a46-398c-b8ae-df67b2f7129e | -19.29184 | -49.68228 | 2024-09-27 04:42:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5512a7df-db0f-3a93-9af5-e55fb9000d9c | -19.29124 | -49.68644 | 2024-09-27 04:42:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e8c22b5-e4df-3be5-a4be-bfdb20806079 | -19.00709 | -49.44978 | 2024-09-27 04:42:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 839be0cb-08dc-35f7-9fe3-6994c1aab9fc | -19.00648 | -49.45403 | 2024-09-27 04:42:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c373faa-ed8d-3faf-9627-c8491d8f7b15 | -19.00355 | -49.44922 | 2024-09-27 04:42:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63e008b3-59df-3a0f-b6ea-e41af5d03be9 | -18.90268 | -50.26825 | 2024-09-27 04:42:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bef8264c-99a7-3820-93c3-399633f5e2f1 | -18.90041 | -50.25986 | 2024-09-27 04:42:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7153601-b623-3f37-84dd-e2454b7324a2 | -18.89983 | -50.26379 | 2024-09-27 04:42:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b048866-1dcb-3183-8c96-c554662f808b | -18.89699 | -50.25932 | 2024-09-27 04:42:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d77f011-f03d-3395-af0d-ac0f7b4550b4 | -18.89356 | -50.25876 | 2024-09-27 04:42:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5429058e-cd26-3e98-a340-4eedb9292a8d | -18.39741 | -49.3153 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 418ee5cb-8663-35a4-b63f-777cf990f350 | -18.39454 | -49.31147 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c70cb37-7ce3-3c88-9d6c-4a5fe85423ef | -18.39446 | -49.31049 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| caca01e8-c82e-37e0-8373-6a4c360f1cfd | -18.39393 | -49.31569 | 2024-09-27 04:42:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README104.md)
